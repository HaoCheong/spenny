#!/bin/bash
# Usage: bash scripts/move_to_pi.sh hao
#        bash scripts/move_to_pi.sh yunshu

OWNER=$1
ENV_FILE="env/${OWNER}_prod.env"
PI_USER="hcheong-pi4-home"
PI_HOST="192.168.0.13"
PI_DIR="/home/hcheong-pi4-home/apps/spenny"

echo "> Running for owner: $OWNER"

# Had to run this to allow building for arm64 (RUN ONCE)
# docker run --privileged --rm tonistiigi/binfmt --install arm64

# 1. Build images locally using the env file
echo "> Building the images locally"
docker compose -f to_prod/docker-compose-prod.yml --env-file $ENV_FILE --profile live build --no-cache
# 2. Load image names from env to reference them
echo "> Loading the env file"
set -a && source $ENV_FILE && set +a

# 3. Stream images directly into the Pi (no temp files)
echo "> Save and load image into PI - BACKEND"
docker save $BACKEND_IMAGE_NAME  | ssh $PI_USER@$PI_HOST docker load
echo "> Save and load image into PI - FRONTEND"
docker save $FRONTEND_IMAGE_NAME | ssh $PI_USER@$PI_HOST docker load

# 4. Push compose file + env file to Pi
echo "> Copy the docker compose"
scp to_prod/docker-compose-prod.yml $PI_USER@$PI_HOST:$PI_DIR/docker-compose.yml
echo "> Copy the env_file"
scp $ENV_FILE $PI_USER@$PI_HOST:$PI_DIR/$ENV_FILE

# # 5. Start on Pi
ssh $PI_USER@$PI_HOST "cd $PI_DIR && docker compose --env-file $ENV_FILE --profile live up -d"