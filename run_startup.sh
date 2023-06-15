#!/bin/bash

# Check if build exists, if no, exit with 1
if [[ "$(docker images -q spenny_backend 2> /dev/null)" == "" ]]; then
    echo "Backend Image does not exist"
    exit 1
fi

if [[ "$(docker images -q spenny_frontend 2> /dev/null)" == "" ]]; then
    echo "Frontend Image does not exist"
    exit 1
fi

# Check if container already running, if yes, stop and rm container
if /usr/bin/docker container inspect spenny_backend_cont > /dev/null 2>&1; then
    /usr/bin/docker stop spenny_backend_cont
    /usr/bin/docker rm spenny_backend_cont
fi

if /usr/bin/docker container inspect spenny_frontend_cont > /dev/null 2>&1; then
    /usr/bin/docker stop spenny_frontend_cont
    /usr/bin/docker rm spenny_frontend_cont
fi

BE_SOURCE_DIR="/home/hcheong/projects/spenny/backend/app"
BE_CONTAINER_IMAGE="spenny_backend"
FE_SOURCE_DIR="/home/hcheong/projects/spenny/frontend"
FE_CONTAINER_IMAGE="spenny_frontend"

# Run container
echo "Starting backend container"
docker run -d \
--mount type=bind,source="${BE_SOURCE_DIR}",target=/app/ \
-p 8000:8000 \
--name "spenny_backend_cont" "${BE_CONTAINER_IMAGE}"

echo "Starting frontend container"
docker run -d \
--restart always \
--mount type=bind,source="${FE_SOURCE_DIR}",target=/app/ \
-p 3000:3000 \
--name "spenny_frontend_cont" "${FE_CONTAINER_IMAGE}"
