#!/bin/bash
# Usage: bash scripts/move_to_pi.sh hao
#        bash scripts/move_to_pi.sh yunshu

set -euo pipefail

OWNER="${1:-}"
if [[ -z "$OWNER" ]]; then
  echo "Usage: $0 <owner>" >&2
  exit 1
fi

ENV_FILE="env/${OWNER}_prod.env"
PI_USER="hcheong-pi4-home"
PI_HOST="192.168.0.13"
PI_DIR="/home/hcheong-pi4-home/apps/spenny"
COMPOSE_FILE="to_prod/docker-compose-prod.yml"
SSH="$PI_USER@$PI_HOST"

[[ -f "$ENV_FILE" ]]     || { echo "Missing env file: $ENV_FILE" >&2; exit 1; }
[[ -f "$COMPOSE_FILE" ]] || { echo "Missing compose file: $COMPOSE_FILE" >&2; exit 1; }

echo "> Running for owner: $OWNER"

# Had to run this to allow building for arm64 (RUN ONCE)
# docker run --privileged --rm tonistiigi/binfmt --install arm64

# Load env early so image names are available for validation and verification.
echo "> Loading the env file"
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

: "${BACKEND_IMAGE_NAME:?BACKEND_IMAGE_NAME not set in $ENV_FILE}"
: "${FRONTEND_IMAGE_NAME:?FRONTEND_IMAGE_NAME not set in $ENV_FILE}"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Layer DiffIDs are content-addressed, so they are identical across machines
# regardless of image store backend (graphdriver vs containerd) or how the tag
# resolves. Image IDs are NOT comparable across machines and must not be used
# for verification.
local_layers()  { docker image inspect --format '{{json .RootFS.Layers}}' "$1"; }
remote_layers() { ssh "$SSH" "docker image inspect --format '{{json .RootFS.Layers}}' '$1'"; }

local_created()  { docker image inspect --format '{{.Created}}' "$1"; }
remote_created() { ssh "$SSH" "docker image inspect --format '{{.Created}}' '$1'"; }

verify_image() {
  local label="$1" image="$2"
  local l_layers r_layers

  l_layers=$(local_layers "$image")
  if ! r_layers=$(remote_layers "$image" 2>/dev/null); then
    echo "ERROR: $label image '$image' does not exist on the Pi at all." >&2
    echo "       The docker load step did not apply the tag. Check its output above." >&2
    return 1
  fi

  if [[ "$l_layers" != "$r_layers" ]]; then
    echo "ERROR: $label layers on the Pi do not match the local build." >&2
    echo "  local  created: $(local_created "$image")" >&2
    echo "  remote created: $(remote_created "$image")" >&2
    echo "  local  layers:  $l_layers" >&2
    echo "  remote layers:  $r_layers" >&2
    echo "       An older remote 'created' timestamp means the load genuinely" >&2
    echo "       did not take effect. Check disk space with: ssh $SSH df -h /var/lib/docker" >&2
    return 1
  fi

  echo "  $label OK (layers match, built $(local_created "$image"))"
}

# ---------------------------------------------------------------------------
# 1. Build
# ---------------------------------------------------------------------------

# Drop --no-cache once you trust the pipeline; it roughly triples build time and
# the layer cache was never the cause of the stale deploys.
echo "> Building the images locally"
docker compose -f "$COMPOSE_FILE" --env-file "$ENV_FILE" --profile live build

# Catch a missing `platform:` in the compose file before shipping a useless image.
for IMG in "$BACKEND_IMAGE_NAME" "$FRONTEND_IMAGE_NAME"; do
  ARCH=$(docker image inspect --format '{{.Architecture}}' "$IMG")
  if [[ "$ARCH" != "arm64" ]]; then
    echo "ERROR: $IMG is $ARCH, expected arm64." >&2
    echo "       Set 'platform: linux/arm64' on the service in $COMPOSE_FILE." >&2
    exit 1
  fi
done
echo "> Architecture check passed (arm64)"

# ---------------------------------------------------------------------------
# 2. Transfer
# ---------------------------------------------------------------------------

# If your local buildx produces a multi-platform index, add --platform linux/arm64
# to the docker save calls below to export only the arm64 child manifest. That
# flag needs a reasonably recent Docker; drop it if your daemon rejects it.
#
# Watch the "Loaded image:" line in the output. If it says "Loaded image ID:"
# with no name, the tag was not applied on the Pi and the verify step will fail.

echo "> Save and load image into PI - BACKEND"
docker save "$BACKEND_IMAGE_NAME" | gzip | ssh "$SSH" "gunzip | docker load"

echo "> Save and load image into PI - FRONTEND"
docker save "$FRONTEND_IMAGE_NAME" | gzip | ssh "$SSH" "gunzip | docker load"

# ---------------------------------------------------------------------------
# 3. Verify
# ---------------------------------------------------------------------------

echo "> Verifying images on the Pi"
verify_image "backend"  "$BACKEND_IMAGE_NAME"
verify_image "frontend" "$FRONTEND_IMAGE_NAME"

# ---------------------------------------------------------------------------
# 4. Push compose + env
# ---------------------------------------------------------------------------

ssh "$SSH" "mkdir -p '$PI_DIR'"
echo "> Copy the docker compose"
scp "$COMPOSE_FILE" "$SSH:$PI_DIR/docker-compose.yml"
echo "> Copy the env_file"
scp "$ENV_FILE" "$SSH:$PI_DIR/prod.env"

# ---------------------------------------------------------------------------
# 5. Start on Pi
# ---------------------------------------------------------------------------

# --env-file is prod.env, the path that exists ON THE PI. The original script
# interpolated the local env/<owner>_prod.env path into the remote command, so
# Compose errored out and the previous containers just kept running.
echo "> Starting on the Pi"
ssh "$SSH" "cd '$PI_DIR' && docker compose --env-file prod.env --profile live up -d --force-recreate --remove-orphans"

echo "> Deployed. Running containers:"
ssh "$SSH" "cd '$PI_DIR' && docker compose --env-file prod.env --profile live ps"

# Optional: reclaim space from the images this deploy orphaned.
# ssh "$SSH" "docker image prune -f"