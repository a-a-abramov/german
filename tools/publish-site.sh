#!/usr/bin/env bash
#
# publish-site.sh — build site/ and push it to the gh-pages branch.
#
# The generated HTML never lands on master: master carries the generator
# (tools/site.py) and the sources it reads, gh-pages carries the output only.
# The branch is built in a throwaway worktree, so your working tree is never
# switched out from under you.
#
#   tools/publish-site.sh            # build, commit, push
#   tools/publish-site.sh --dry-run  # build and stage, show the diff, push nothing
#
set -euo pipefail

BRANCH=gh-pages
DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"

python3 tools/site.py

WT="$(mktemp -d)/$BRANCH"

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
    git worktree add "$WT" "$BRANCH" >/dev/null
elif git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
    git fetch origin "$BRANCH:$BRANCH"
    git worktree add "$WT" "$BRANCH" >/dev/null
else
    echo "  creating $BRANCH (orphan)"
    git worktree add --detach "$WT" >/dev/null
    git -C "$WT" checkout --orphan "$BRANCH" >/dev/null
    git -C "$WT" rm -rf . >/dev/null 2>&1 || true
fi

cleanup() { git worktree remove --force "$WT" >/dev/null 2>&1 || true; }
trap cleanup EXIT

# the branch is the output, nothing else: drop whatever the last build left
find "$WT" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -R site/. "$WT/"

cd "$WT"
git add -A

if git diff --cached --quiet; then
    echo "  site unchanged — nothing to publish"
    exit 0
fi

git diff --cached --stat | tail -3

if [ "$DRY" = 1 ]; then
    echo "  dry run — not committing"
    exit 0
fi

git commit -q -m "Publish site from $(git -C "$ROOT" rev-parse --short HEAD)"
git push -q -u origin "$BRANCH"
echo "  pushed to $BRANCH → https://a-a-abramov.github.io/german/"
