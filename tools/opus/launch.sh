#!/usr/bin/env bash
# launch.sh — start (or resume) the overnight parse on atlas. Safe to re-run:
# shards that already have a .done marker are skipped, so nothing is recomputed.
#
#   ssh andrey@192.168.88.5 '/home/andrey/opus-de/code/launch.sh'
#
# then disconnect. In the morning:
#
#   ssh andrey@192.168.88.5 '/home/andrey/opus-de/code/morning.sh'
#
# --network=none is not caution, it is a proof: spaCy and de_core_news_sm are baked
# into the image at build time, so the run cannot fail at 3am because a download 404'd.
#
# The log is tee'd to /home/andrey/opus-de/work/logs/ as well as going to podman logs,
# because `podman logs` dies with the container and the log is the whole diagnostic.
set -euo pipefail

BASE=/home/andrey/opus-de
JOBS=${JOBS:-3}                  # 4 cores; leave one for grafana/prometheus/zfs
HOURS=${HOURS:-8}
MEM=${MEM:-7g}
NAME=${NAME:-wp-night}
STAMP=$(date +%Y%m%d-%H%M%S)

mkdir -p "$BASE/work/logs" "$BASE/work/counts" "$BASE/work/merged"

if [ ! -d "$BASE/work/shards" ] || [ -z "$(ls -A "$BASE/work/shards" 2>/dev/null)" ]; then
    echo "ERROR: no shards in $BASE/work/shards — run prepare.py first." >&2
    exit 1
fi

if podman container exists "$NAME" 2>/dev/null; then
    echo "removing previous container $NAME"
    podman rm -f "$NAME" >/dev/null
fi

podman run -d --name "$NAME" \
    --network=none \
    --memory="$MEM" --cpus=3.5 \
    --userns=keep-id \
    -v "$BASE/code:/code:ro" \
    -v "$BASE/work:/work" \
    -w /code \
    wortprofil:de \
    sh -c "python /code/run_night.py --jobs $JOBS --deadline-hours $HOURS 2>&1 \
           | tee /work/logs/night-$STAMP.log"

ln -sfn "$BASE/work/logs/night-$STAMP.log" "$BASE/work/logs/latest.log"

cat <<EOF
started $NAME  (jobs=$JOBS  deadline=${HOURS}h  mem=$MEM)

  follow:  podman logs -f $NAME
  log:     $BASE/work/logs/night-$STAMP.log  (also work/logs/latest.log)
  morning: $BASE/code/morning.sh
  result:  $BASE/work/merged/wp.db
EOF
