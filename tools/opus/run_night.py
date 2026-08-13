#!/usr/bin/env python3
"""
run_night.py — the unsupervised driver. Start it, disconnect, read the log in the morning.

Design constraints, all of them consequences of "nobody is watching":

  * DEADLINE, NOT SHARD COUNT. Shards are round-robin samples of the whole corpus
    (see prepare.py), so stopping early costs sample size, not representativeness.
    At --deadline-hours the driver stops launching new shards, lets running ones
    finish, and proceeds to merge. You get a finished database either way.

  * ONE SUBPROCESS PER SHARD, not a process pool. If a worker is OOM-killed, a pool
    raises BrokenProcessPool and takes down every sibling; a subprocess just returns
    non-zero and the driver logs it and carries on. Model load is ~3s against a
    ~10min shard, so the repeated startup is noise.

  * MERGE RUNS AUTOMATICALLY. The whole point is to wake up to wp.db, not to a
    directory of count files needing a second command.

  * RESUMABLE. Re-running skips shards with a .done marker. Safe to launch again after
    a reboot, a crash, or a deliberate stop.

  * THE LOG HAS TO EXPLAIN ITSELF THE NEXT MORNING. Nobody will be watching when it
    goes wrong, so the log carries the run manifest, a 5-minute heartbeat with memory
    and disk, and the tail of any failed worker's own log inlined — not a pointer to a
    file that may itself be the thing that's missing. run_state.json holds the same
    information in machine-readable form.
"""

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
HEARTBEAT = 300


def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}", flush=True)


def read_int(path):
    try:
        with open(path) as f:
            return int(f.read().strip())
    except Exception:
        return -1


def resources(workdir):
    """cgroup memory is the number that matters — it is what the --memory cap kills on."""
    cur = read_int("/sys/fs/cgroup/memory.current")
    peak = read_int("/sys/fs/cgroup/memory.peak")
    mx = read_int("/sys/fs/cgroup/memory.max")
    du = shutil.disk_usage(workdir)
    return {
        "mem_current_gb": round(cur / 2**30, 2) if cur > 0 else None,
        "mem_peak_gb": round(peak / 2**30, 2) if peak > 0 else None,
        "mem_limit_gb": round(mx / 2**30, 2) if mx > 0 else None,
        "disk_free_gb": round(du.free / 2**30, 1),
        "counts_dir_gb": round(dir_size(workdir) / 2**30, 2),
    }


def dir_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for fn in files:
            try:
                total += os.path.getsize(os.path.join(root, fn))
            except OSError:
                pass
    return total


def tail(path, n=25):
    try:
        with open(path, errors="replace") as f:
            return "".join(f.readlines()[-n:]).rstrip()
    except Exception as e:
        return f"<could not read {path}: {e}>"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--shards", default="/work/shards")
    p.add_argument("--counts", default="/work/counts")
    p.add_argument("--db", default="/work/merged/wp.db")
    p.add_argument("--jobs", type=int, default=3,
                   help="parallel workers; leave a core for the host's services")
    p.add_argument("--deadline-hours", type=float, default=8.0)
    p.add_argument("--max-shards", type=int, default=0, help="0 = all")
    p.add_argument("--no-merge", action="store_true")
    args = p.parse_args()

    os.makedirs(args.counts, exist_ok=True)
    state_path = os.path.join(args.counts, "run_state.json")
    t0 = time.time()
    deadline = t0 + args.deadline_hours * 3600

    all_shards = sorted(glob.glob(os.path.join(args.shards, "shard_*.txt.gz")))
    if args.max_shards:
        all_shards = all_shards[:args.max_shards]
    todo = [s for s in all_shards
            if not os.path.exists(os.path.join(
                args.counts, os.path.basename(s).replace(".txt.gz", "") + ".done"))]

    # ---- run manifest: everything needed to reproduce or diagnose this run ----
    import spacy
    manifest = {
        "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "deadline": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(deadline)),
        "deadline_hours": args.deadline_hours,
        "jobs": args.jobs,
        "shards_total": len(all_shards),
        "shards_todo": len(todo),
        "spacy": spacy.__version__,
        "python": sys.version.split()[0],
        "cpu_count": os.cpu_count(),
        "resources_at_start": resources(args.counts),
    }
    log("=" * 72)
    log("RUN MANIFEST")
    for k, v in manifest.items():
        log(f"  {k:22} {v}")
    log("=" * 72)

    running, queue, failed, finished = {}, list(todo), [], 0
    tok_total = sent_total = 0
    last_beat = 0.0
    deadline_announced = False

    def save_state(phase):
        try:
            with open(state_path, "w") as f:
                json.dump({
                    "phase": phase,
                    "manifest": manifest,
                    "elapsed_hours": round((time.time() - t0) / 3600, 2),
                    "finished": finished, "failed": failed,
                    "queued": len(queue), "running": [v[0] for v in running.values()],
                    "tokens_parsed": tok_total, "sentences_parsed": sent_total,
                    "resources": resources(args.counts),
                    "updated": time.strftime("%Y-%m-%d %H:%M:%S"),
                }, f, indent=2)
        except Exception as e:
            log(f"(could not write run_state.json: {e})")

    while queue or running:
        while queue and len(running) < args.jobs and time.time() < deadline:
            shard = queue.pop(0)
            name = os.path.basename(shard)
            logf = open(os.path.join(args.counts, name.replace(".txt.gz", ".log")), "w")
            proc = subprocess.Popen(
                [sys.executable, os.path.join(HERE, "parse_shard.py"), shard, args.counts],
                stdout=logf, stderr=subprocess.STDOUT)
            running[proc] = (name, logf, time.time())
            log(f"launched {name} ({len(queue)} queued, {len(running)} running)")

        if queue and time.time() >= deadline and not deadline_announced:
            log(f"DEADLINE reached after {args.deadline_hours}h — dropping "
                f"{len(queue)} unstarted shards; {len(running)} running will finish. "
                f"Re-run launch.sh later to process them; nothing is lost.")
            queue, deadline_announced = [], True

        time.sleep(5)

        for proc in list(running):
            if proc.poll() is None:
                continue
            name, logf, started = running.pop(proc)
            logf.close()
            logpath = os.path.join(args.counts, name.replace(".txt.gz", ".log"))
            if proc.returncode == 0:
                finished += 1
                try:
                    m = json.load(open(os.path.join(
                        args.counts, name.replace(".txt.gz", ".done"))))
                    tok_total += m["tokens"]
                    sent_total += m["sentences"]
                    rate = f'{m["tokens_per_sec"]:,} tok/s'
                except Exception:
                    rate = "rate unknown"
                left = len(queue) + len(running)
                per = (time.time() - t0) / max(finished, 1)
                log(f"OK   {name} {time.time()-started:.0f}s {rate} — "
                    f"{finished} done, {left} left, ETA {per*left/3600:.1f}h, "
                    f"{tok_total:,} tok so far")
            else:
                failed.append(name)
                # Inline the worker's own tail: in the morning this log must explain
                # the failure by itself, without a hunt through 200 sibling files.
                log(f"FAIL {name} rc={proc.returncode} after {time.time()-started:.0f}s "
                    f"(continuing). Its log said:\n"
                    + "\n".join("      | " + ln for ln in tail(logpath).splitlines()))

        if time.time() - last_beat > HEARTBEAT:
            last_beat = time.time()
            r = resources(args.counts)
            el = (time.time() - t0) / 3600
            log(f"heartbeat  {el:.2f}h elapsed | done={finished} fail={len(failed)} "
                f"queued={len(queue)} running={len(running)} | {tok_total:,} tok | "
                f"mem {r['mem_current_gb']}/{r['mem_limit_gb']} GB "
                f"(peak {r['mem_peak_gb']}) | disk free {r['disk_free_gb']} GB | "
                f"counts {r['counts_dir_gb']} GB")
            save_state("parsing")

    parse_hours = (time.time() - t0) / 3600
    log("-" * 72)
    log(f"PARSE PHASE DONE in {parse_hours:.2f}h — {finished} ok, {len(failed)} failed")
    log(f"  {sent_total:,} sentences, {tok_total:,} tokens parsed")
    if failed:
        log(f"  failed shards: {failed}")
    log(f"  resources: {resources(args.counts)}")
    save_state("parsed")

    if args.no_merge:
        return 0

    log("-" * 72)
    log("MERGE + SCORE phase starting")
    mt0 = time.time()
    rc = subprocess.call([sys.executable, os.path.join(HERE, "merge_score.py"),
                          args.counts, args.db])
    log(f"merge exited rc={rc} after {(time.time()-mt0)/60:.1f} min")
    if rc == 0 and os.path.exists(args.db):
        log(f"  database: {args.db} "
            f"({os.path.getsize(args.db)/2**30:.2f} GB)")
    else:
        log("  MERGE FAILED — the per-shard counts in /work/counts are intact. "
            "Re-run merge_score.py alone; no need to re-parse.")
    save_state("done" if rc == 0 else "merge_failed")
    log(f"TOTAL WALL TIME {(time.time()-t0)/3600:.2f}h")
    log("=" * 72)
    return rc


if __name__ == "__main__":
    sys.exit(main())
