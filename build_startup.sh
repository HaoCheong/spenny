  
# Builds images on first run, rebuild on subsequent run
  
#!/bin/bash

ABS_PATH=$("pwd")
BE_DOCKER_PATH="${ABS_PATH}/backend/"
BE_IMAGE="spenny_backend_img"
BE_CONT="spenny_backend_cont"
  
FE_DOCKER_PATH="${ABS_PATH}/frontend/"
FE_IMAGE="spenny_frontend_img"
FE_CONT="spenny_frontend_cont"
  
# Remove backend images
if docker image inspect ${BE_IMAGE} > /dev/null 2>&1; then
    echo "Clearing backend image"
    docker stop ${BE_CONT}
    docker rm ${BE_CONT}
    docker rmi ${BE_IMAGE}
fi
  
# Remove frontend images
if docker image inspect ${FE_IMAGE} > /dev/null 2>&1; then
	echo "Clearing frontend image"
	docker stop ${FE_CONT}
	docker rm ${FE_CONT}
	docker rmi ${FE_IMAGE}
fi
  
# Build backend image
echo "Building backend image"
docker build -t ${BE_IMAGE} ${BE_DOCKER_PATH}
  
# Build frontend image
echo "Building frontend image"
docker build -t ${FE_IMAGE} ${FE_DOCKER_PATH}
