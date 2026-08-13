# tools/opus — the Wortprofil build pipeline

Builds `opus-de/wp.db` from OPUS OpenSubtitles on the server `atlas` (192.168.88.5),
in a rootless podman container with nothing installed on the host.

**Two documents, depending on what you need:**

- **[`../../WORTPROFIL.md`](../../WORTPROFIL.md)** — how to *query* the database.
  Start here if you just want collocations.
- **[`IMPLEMENTATION.md`](IMPLEMENTATION.md)** — data structures, the empirical relation
  model, and why the code departs from the recipe in seven places. Read before changing
  anything here.

## Files

| file | role |
|---|---|
| `Containerfile` | the environment; spaCy + de_core_news_sm baked in at build time |
| `probe_labels.py`, `probe2.py` | Step 3a — what the parser *actually* emits |
| `extract.py` | the dependency → relation mapping (the real content) |
| `test_extract.py` | **the gate** — 21 assertions incl. row direction and the aux hop |
| `prepare.py` | clean, dedup, hash-sample, round-robin shard |
| `parse_shard.py` | parse one shard → three count tables (pairs + both marginals) |
| `merge_score.py` | streaming k-way merge → logDice → SQLite |
| `run_night.py` | unsupervised driver: deadline, restarts, heartbeat, auto-merge |
| `launch.sh` | start or resume the run (resumable, skips finished shards) |
| `morning.sh` | one-command status report for the finished run |

## The gate

Run this in the container after any change to `extract.py`. It must print 21/21 — it
encodes the four ways the recipe's dependency-label table is wrong, and it renders through
the real `RELATION_PATTERNS` so a reversed row fails here instead of in a text weeks later.

```bash
ssh andrey@192.168.88.5 'podman run --rm --network=none \
    -v /home/andrey/opus-de/code:/code:ro --userns=keep-id -w /code \
    wortprofil:de python /code/test_extract.py'
```

Changing `extract.py` invalidates existing counts — delete `work/counts/*` rather than
mixing rule sets across shards. Changing only `MIN_PAIR` or the scoring needs no re-parse.
