#!/bin/bash

#########################################################
########## CONTAINER MANAGEMENT UTILITY SCRIPT ##########
#########################################################


function remove_containers  {

    # Remove running containers if they exist

    container=$1
    
    if docker container inspect $container > /dev/null 2>&1; then
        echo "> Stop and Remove Container - ${container}"
        docker stop $container
        docker rm $container
    else
        echo "> Container already removed - Container: ${container}"
    fi
}

function pull_image {

    # Pull image if it does not exist

    image=$1

    if !docker image inspect $image > /dev/null 2>&1; then
        echo "> Pulling Image - IMAGE: ${image}"
        docker pull $image
    else
        echo "> Image already exist locally - Image: ${image}"
    fi
}

function remove_image {

    image=$1
    
    docker image inspect $image

    # Remove image if they exist
    if [[ $? -eq 0 ]]; then
        echo "> Removing Image - Image: ${image}"
        docker rmi -f $image
    else
        echo "> Image already removed - Image: ${image}"
    fi
}

function build_image {
    # Build an image given a path (Different from pulling a container)

    image=$1
    image_path=$2
    dockerfile_name=$3

    docker image inspect $image

    if [[ $? -eq 1 ]]; then
        echo "========== BUILDING IMAGE - ${image}, ${image_path} =========="
        docker build -f $dockerfile_name -t $image $image_path
    else
        echo "> Image already built - ${image}, ${image_path}"
    fi
    
}

function show_config {
    # Shows the configuration values currently set

    echo "PROJECT_NAME: ${PROJECT_NAME}"
    echo "LOCAL_PROJECT_PATH: ${LOCAL_PROJECT_PATH}"
    echo "=============================="
    echo "SMS_POSTGRES_DB_USER: ${SMS_POSTGRES_DB_USER}"
    echo "SMS_POSTGRES_DB_PASS: ${SMS_POSTGRES_DB_PASS}"
    echo "SMS_POSTGRES_DB_NAME: ${SMS_POSTGRES_DB_NAME}"
    echo "SMS_POSTGRES_DB_HOST: ${SMS_POSTGRES_DB_HOST}"
    echo "SMS_POSTGRES_DB_PORT: ${SMS_POSTGRES_DB_PORT}"
    echo "=============================="
    echo "SMS_SQL_DUMP_FILE_PATH: ${SMS_SQL_DUMP_FILE_PATH}"
    echo "SMS_SQL_DUMP_SCHEMA_ONLY: ${SMS_SQL_DUMP_SCHEMA_ONLY}"
    echo "=============================="
    echo "SMS_CONTAINER_NAME: ${SMS_CONTAINER_NAME}"
    echo "SMS_IMAGE_NAME: ${SMS_IMAGE_NAME}"
    echo "=============================="
    echo "SMS_TIMEZONE: ${SMS_TIMEZONE}"
    echo "=============================="
    echo "SMS_AUTH_CLIENT_ID: ${SMS_AUTH_CLIENT_ID}"
    echo "SMS_AUTH_CLIENT_SECRET: ${SMS_AUTH_CLIENT_SECRET}"
    echo "SMS_AUTH_TENANT_ID: ${SMS_AUTH_TENANT_ID}"
    echo "SMS_AUTH_REDIRECT_URL: ${SMS_AUTH_REDIRECT_URL}"
    echo "SMS_AUTH_SCOPE: ${SMS_AUTH_SCOPE}"
    echo "=============================="
    echo "AIRSIG_POSTGRES_DB_USER: ${AIRSIG_POSTGRES_DB_USER}"
    echo "AIRSIG_POSTGRES_DB_PASS: ${AIRSIG_POSTGRES_DB_PASS}"
    echo "AIRSIG_POSTGRES_DB_NAME: ${AIRSIG_POSTGRES_DB_NAME}"
    echo "AIRSIG_POSTGRES_DB_HOST: ${AIRSIG_POSTGRES_DB_HOST}"
    echo "AIRSIG_POSTGRES_DB_PORT: ${AIRSIG_POSTGRES_DB_PORT}"
    echo "=============================="
    echo "AIRSIG_SQL_DUMP_PATH: ${AIRSIG_SQL_DUMP_PATH}"
    echo "AIRSIG_SQL_DUMP_SCHEMA_ONLY: ${AIRSIG_SQL_DUMP_SCHEMA_ONLY}"
    echo "=============================="
    echo "AIRSIG_CONTAINER_NAME: ${AIRSIG_CONTAINER_NAME}"
    echo "AIRSIG_IMAGE_NAME: ${AIRSIG_IMAGE_NAME}"
    echo "=============================="
    echo "AIRSIG_TIMEZONE: ${AIRSIG_TIMEZONE}"
    echo "=============================="
    echo "BACKEND_PORT: ${BACKEND_PORT}"
    echo "BACKEND_APP_PATH: ${BACKEND_APP_PATH}"
    echo "BACKEND_CONTAINER_URL: ${BACKEND_CONTAINER_URL}"
    echo "BACKEND_CONTAINER_NAME: ${BACKEND_CONTAINER_NAME}"
    echo "BACKEND_IMAGE_NAME: ${BACKEND_IMAGE_NAME}"
    echo "BACKEND_TIMEZONE: ${BACKEND_TIMEZONE}"
    echo "=============================="
    echo "BACKEND_CONFIG_PATH: ${BACKEND_CONFIG_PATH}"
    echo "BACKEND_LOG_PATH: ${BACKEND_LOG_PATH}"
    echo "BACKEND_ENV: ${BACKEND_ENV}"
    echo "=============================="
    echo "FRONTEND_PORT: ${FRONTEND_PORT}"
    echo "FRONTEND_APP_PATH: ${FRONTEND_APP_PATH}"
    echo "FRONTEND_CONTAINER_URL: ${FRONTEND_CONTAINER_URL}"
    echo "FRONTEND_CONTAINER_NAME: ${FRONTEND_CONTAINER_NAME}"
    echo "FRONTEND_IMAGE_NAME: ${FRONTEND_IMAGE_NAME}"
    echo "FRONTEND_TIMEZONE: ${FRONTEND_TIMEZONE}"
    echo "========== END =========="
}

function show_container_status {
    # Displays the container status

    echo "========== CONTAINERS STATUS =========="
    docker ps
}

function show_container_url {
    # Displays the access container for required access

    container_url=$1
    container_name=$2

    echo "========== ACCESS URL for CONTAINER: ${container_name} =========="
    echo "> ${container_url}"
}

function run_container {

    # Spin up a blank container

    container_name=$1
    image_name=$2

    expose_port=$3
    timezone=$4

    

    # Run container
    if docker container inspect $container_name > /dev/null 2>&1; then
        echo "> Container already running - Container: ${container_name}"
    else
        echo "> Running Container - Container: ${container_name}"
        docker run\
            -d \
            -e TZ=$timezone\
            -p $expose_port:8000\
            --name $container_name $image_name
    fi

    sleep 2 # Buffer to let it start up internally
}