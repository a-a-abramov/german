#!/usr/bin/env bash
# morning.sh — everything needed to judge the overnight run, in one output.
# Written to be pasted wholesale into a chat: no interactive paging, bounded length.
#
#   ssh andrey@192.168.88.5 '/home/andrey/opus-de/code/morning.sh'
BASE=/home/andrey/opus-de
W=$BASE/work

hr() { printf '\n===== %s =====\n' "$1"; }

hr "CONTAINER"
podman ps -a --filter name=wp-night --format '{{.Names}}  {{.Status}}  {{.Exited}}' 2>&1

hr "RUN STATE"
cat "$W/counts/run_state.json" 2>&1

hr "MANIFEST + HEARTBEATS + FAILURES (from the driver log)"
if [ -f "$W/logs/latest.log" ]; then
    grep -E 'MANIFEST|^\s+[a-z_]+ +|heartbeat|FAIL|DEADLINE|PARSE PHASE|MERGE|TOTAL|database:|\|' \
        "$W/logs/latest.log" | tail -60
else
    echo "no driver log at $W/logs/latest.log"
fi

hr "LAST 30 LINES OF DRIVER LOG"
tail -30 "$W/logs/latest.log" 2>&1

hr "SHARD TALLY"
echo "shards prepared : $(ls "$W/shards"/shard_*.txt.gz 2>/dev/null | wc -l)"
echo "shards done     : $(ls "$W/counts"/*.done 2>/dev/null | wc -l)"
echo "counts size     : $(du -sh "$W/counts" 2>/dev/null | cut -f1)"

hr "THROUGHPUT PER SHARD (slowest 5, fastest 5)"
cat "$W/counts"/*.done 2>/dev/null | python3 -c "
import sys, json
ms = [json.loads(l) for l in sys.stdin.read().replace('}{', '}\n{').splitlines() if l.strip()]
if not ms:
    print('none yet'); raise SystemExit
ms.sort(key=lambda m: m['tokens_per_sec'])
tot_t = sum(m['tokens'] for m in ms); tot_s = sum(m['sentences'] for m in ms)
print(f'{len(ms)} shards, {tot_s:,} sentences, {tot_t:,} tokens')
print(f'median rate {ms[len(ms)//2][\"tokens_per_sec\"]:,} tok/s/worker')
for m in ms[:5] + ms[-5:]:
    print(f'  {m[\"shard\"]}  {m[\"tokens_per_sec\"]:>7,} tok/s  {m[\"seconds\"]:>6.0f}s  '
          f'{m[\"distinct_pairs\"]:>9,} pairs')
" 2>&1

hr "WORKER ERRORS (any traceback in a shard log)"
grep -l -E 'Traceback|Error|Killed' "$W/counts"/*.log 2>/dev/null | head -10 | while read -r f; do
    echo "--- $f"; tail -15 "$f"
done
echo "(none listed above = no worker errors)"

hr "DATABASE"
if [ -f "$W/merged/wp.db" ]; then
    ls -lh "$W/merged/wp.db"
    podman run --rm -i --network=none -v "$W:/work" --userns=keep-id wortprofil:de python - <<'PY' 2>&1
import sqlite3
db = sqlite3.connect("file:/work/merged/wp.db?mode=ro", uri=True)
print("-- meta --")
for k, v in db.execute("SELECT k, v FROM meta ORDER BY k"):
    print(f"  {k:30} {v}")
print("-- rows per relation --")
for rel, n in db.execute("SELECT relation, count(*) FROM colloc GROUP BY relation "
                         "ORDER BY count(*) DESC"):
    print(f"  {n:>10,}  {rel}")
print("-- freq/logDice distribution (how to set the floors) --")
for f in (3, 5, 10, 20, 50, 100):
    n = db.execute("SELECT count(*) FROM colloc WHERE freq >= ?", (f,)).fetchone()[0]
    print(f"  freq >= {f:<4} {n:>12,}")
for d in (0, 2, 3, 4, 5, 6):
    n = db.execute("SELECT count(*) FROM colloc WHERE logdice >= ?", (d,)).fetchone()[0]
    print(f"  dice >= {d:<4} {n:>12,}")
print("-- SANITY: the three words the recipe says to eyeball --")
for w in ("Wohnung", "Tasse", "Schrank", "Bett", "Kaffee"):
    rows = db.execute(
        "SELECT relation, collocate, round(logdice,1), freq, case_ FROM colloc "
        "WHERE headword=? AND freq>=10 ORDER BY logdice DESC LIMIT 8", (w,)).fetchall()
    print(f"  {w}:")
    for r in rows:
        print(f"     {r[1]:<24} {r[0]:<32} dice={r[2]:<5} f={r[3]:<6} {r[4]}")
    if not rows:
        print("     (nothing — suspicious)")
PY
else
    echo "NO DATABASE at $W/merged/wp.db"
    echo "If the parse phase finished, re-run the merge alone (no re-parsing needed):"
    echo "  podman run --rm --network=none -v $BASE/code:/code:ro -v $W:/work \\"
    echo "    --userns=keep-id wortprofil:de python /code/merge_score.py /work/counts /work/merged/wp.db"
fi

hr "HOST"
free -h; df -h /home | tail -1; uptime
