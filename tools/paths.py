"""
paths.py — every repo path the tools need, in one place.

The tools used to derive each other's paths by chaining `os.path.dirname` off
whichever constant happened to be nearby (`REPO_CSV` hung off the DWDS cache
directory, for one), so moving any single directory silently moved others.
Everything is now anchored to ROOT and nothing else.

Import it as a sibling module — the tools are run as `python3 tools/<name>.py`,
so `tools/` is already on sys.path:

    from paths import VOCAB_DB, GOETHE_CSV
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The plan and the bookkeeping: what is to be learned, and how far along it is.
CURRICULUM  = os.path.join(ROOT, "curriculum")
GOETHE_CSV  = os.path.join(CURRICULUM, "goethe-b1-wortliste.csv")
VOCAB_DB    = os.path.join(CURRICULUM, "vocab.db")
ASSIGNMENTS = os.path.join(CURRICULUM, "assignments.tsv")
GLUE_POOL   = os.path.join(CURRICULUM, "glue-pool.md")

# The study material itself — one directory per batch, `NN-<slug>`.
CONTENT = os.path.join(ROOT, "content")
BATCHES = os.path.join(CONTENT, "batches")

# Downloaded / derived corpora. Git-ignored, rebuildable, never committed.
DATA          = os.path.join(ROOT, "data")
DWDS_CACHE    = os.path.join(DATA, "dwds")
LEIPZIG_CACHE = os.path.join(DWDS_CACHE, "leipzig")
WORTPROFIL_DB = os.path.join(DATA, "wortprofil.db")
