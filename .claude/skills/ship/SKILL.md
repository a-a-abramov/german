---
name: ship
description: Commit the working tree to master, rebuild the reader, and push both master and gh-pages. Use when asked to ship, publish, deploy, "commit and push", "push the site", "update the site", or "publish the reader".
---

# Shipping the repo

One pass: master gets the source commits, `tools/publish-site.sh` regenerates the
reader and pushes it to `gh-pages`, both branches end up on `origin`.

Being invoked *is* the authorization to commit and push, and **master is the
intended target** — do not branch off, do not stop to ask whether committing to
master is allowed. Everything else still needs the usual care: read the diff
before you write a message about it.

## Order matters

    1. commit master
    2. push master
    3. tools/publish-site.sh          (builds, commits gh-pages, pushes gh-pages)

`publish-site.sh` stamps its commit `Publish site from <master short SHA>`, so
master must be **committed before** the script runs, or the site commit cites the
previous revision. Push master **before** the script too: otherwise gh-pages lands
on the remote citing a SHA that isn't reachable there, and a master push that then
needs a rebase leaves that citation permanently wrong.

The script pushes `gh-pages` itself. **Do not push gh-pages separately** — there is
nothing left to push after step 3.

## 1. Commit master

Preconditions — abort and say why if either fails:

- `git rev-parse --abbrev-ref HEAD` is `master`. (The repo keeps writing worktrees
  on side branches; shipping from one is a mistake, not a thing to work around.)
- There is something to commit. If the tree is clean, skip to **step 2**, not
  step 3: master may hold unpushed commits, and the site must never cite a SHA
  the remote doesn't have. `git push` on an up-to-date branch is a harmless no-op.

Read the whole diff before writing anything: `git status --short`, then
`git diff` for the modified text files. `git diff` does not show untracked files —
read anything `git status` marks `??` directly.

**Group into coherent commits.** One commit when the change is one thing; several
when the diff spans unrelated surfaces. In this repo the surfaces that should not
be mixed are:

| surface | paths |
|---|---|
| content | `content/batches/**` |
| the ledger | `curriculum/vocab.db` |
| tools | `tools/**` |
| skills / docs | `.claude/skills/**`, `docs/**`, `README.md` |

The ledger is the exception that travels: a coverage change recorded by
`vocab.py scan --apply` belongs **with** the texts that caused it, in the same
commit. A ledger change with no accompanying text change (a `skip`, a hand
`use`, a re-`init`) is its own commit.

Stage each group explicitly — `git add <the paths for that surface>`. **`git add -A`
is wrong here**: it collapses the split into one commit while looking like the rule
was followed.

`site/` is git-ignored, so no generated HTML can reach master. Never `git add -f`
it.

### The commit message

Read `git log -5` first and match what you see — the convention below is a
description of this repo's history, not a template that outranks it.

- **Subject**: the surface, then the change.
  `Reader: count coverage the same way on every page`,
  `Write batch 2 (Körper & Gesundheit): scenes and dialogues`.
- **Body**: prose or dash bullets saying *what was wrong and why this is the fix* —
  not a list of touched files, which the diff already shows. Carry the concrete
  numbers: `97% vs 96%`, `75 → 92 headwords`, `125 of 128 target words (98%)`.
- **Trailer**: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

`curriculum/vocab.db` is binary, so its diff tells you nothing. Get the numbers
from `python3 tools/vocab.py status` (corpus-wide coverage) and
`python3 tools/vocab.py words --batch N` for the batch in play, and write the
delta into the message.

## 2. Push master

    git push origin master

If it is rejected as non-fast-forward, stop and report it. Do not force-push and
do not rebase without saying so — the gh-pages SHA citation depends on the master
commit you just made staying put.

## 3. Publish the site

    tools/publish-site.sh

It regenerates `site/` with `tools/site.py`, copies it into a throwaway worktree of
`gh-pages`, commits, and pushes. Expected outcomes:

- `pushed to gh-pages → https://a-a-abramov.github.io/german/` — done.
- `site unchanged — nothing to publish` — also fine; report it as a no-op rather
  than retrying.
- `git worktree add` fails with *already used by worktree* — a previous run died
  before its cleanup trap. `git worktree prune`, then run the script again.
- `tools/site.py` raises — the reader build is broken. Master is already committed
  and pushed at this point, which is correct; report the traceback and stop.
  Do not patch site.py inside this skill's run unless asked.

`tools/publish-site.sh --dry-run` builds and stages without committing or pushing.
Use it when the user wants to preview what the site commit would contain.

## Reporting back

One short paragraph: what got committed to master (subjects, one per line), and
what happened to the site — published, or unchanged. Include the gh-pages URL when
something was actually published.
