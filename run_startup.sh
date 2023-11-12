# Run Container on first run, rerun container on subsequent
  
#!/bin/bash
ABS_PATH=$("pwd")
BE_DOCKER_PATH="${ABS_PATH}/backend/app"
BE_IMAGE="spenny_backend_img"
BE_CONT="spenny_backend_cont"
  
FE_DOCKER_PATH="${ABS_PATH}/frontend/"
FE_IMAGE="spenny_frontend_img"
FE_CONT="spenny_frontend_cont"
  
  
# Stop and remove backend container
if docker container inspect ${BE_CONT} > /dev/null 2>&1; then
	echo "Stop and Remove - Spenny Backend Container"
	docker stop ${BE_CONT}
	docker rm ${BE_CONT}
fi
  
# Stop and remove frontend container
if docker container inspect ${FE_CONT} > /dev/null 2>&1; then
	echo "Stop and Remove - Spenny Frontend Container"
	docker stop ${FE_CONT}
	docker rm ${FE_CONT}
fi

if [ "$1" != "stop" ]; then
	# Run Backend
	docker run -p 9101:8000 \
	-d \
	--mount type=bind,source="${BE_DOCKER_PATH}",target=/app/ \
	--name ${BE_CONT} ${BE_IMAGE}
	
	# # Run Frontend
	docker run -p 9102:3000 \
	-d \
	--mount type=bind,source="${FE_DOCKER_PATH}",target=/app/ \
	--name ${FE_CONT} ${FE_IMAGE}
fi
