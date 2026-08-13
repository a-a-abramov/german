# dwds-cache/

Scratch directory for `tools/wortprofil.py`. **Git-ignored — nothing here is committed.**

Two kinds of file land here:

1. **Wortprofil pages you saved yourself.** Open e.g.
   `https://www.dwds.de/wp/?q=Tasse&pos=Substantiv&minfreq=20&minstat=3&limit=25&view=table&mode=full`
   in a browser, then `Cmd-S` → *"Web Page, HTML Only"* → `dwds-cache/Tasse.html`.

   Do **not** fetch these with a script. `https://www.dwds.de/robots.txt` carries
   `Disallow: /wp` for every user-agent plus an explicit legal notice forbidding
   automated access without consent. To request that consent (worth doing —
   it collapses a per-word manual job into one command), write to **dwds@bbaw.de**.

2. **`goethe-A1.json` / `goethe-A2.json` / `goethe-B1.json`** — fetched automatically
   from `https://www.dwds.de/api/lemma/goethe/*.json`, a documented public API endpoint.
   These are the official Goethe-Institut wordlists and are copyrighted; personal use only.
   Remember they are **incremental** — a B1 learner's vocabulary is the union of all three.

3. **`dwds_lemmata.csv`** (~27 MB) — the DWDS Lemmadatenbank, downloaded once by
   `tools/wordfreq.py` from `https://www.dwds.de/lemma/csv`, the offered download linked
   from https://www.dwds.de/lemma/list. 279,346 lemmas with a frequency band each.
   `/lemma` is not robots-disallowed. Personal use; observe the DWDS Nutzungsbedingungen.

4. **`frequency-hits.json`** — per-word raw hit counts from `/api/frequency`, cached so a
   word is never requested twice. The fetcher waits 1.5 s between calls.

See `groundwork/dwds-wortprofil-guide.md` for the full method.
