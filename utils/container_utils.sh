#!/bin/bash

#########################################################
########## CONTAINER MANAGEMENT UTILITY SCRIPT ##########
#########################################################


function remove_containers  {

    # Remove running containers if they exist

    container=$1
    
    if docker container inspect $container > /dev/null 2>&1; then
        echo "> Stop and Remove Container - ${container}"
        docker stop $container > /dev/null 2>&1
        docker rm $container > /dev/null 2>&1
    else
        echo "> Container already removed - Container: ${container}"
    fi
}

function pull_image {

    # Pull image if it does not exist

    image=$1

    if !docker image inspect $image > /dev/null 2>&1; then
        echo "> Pulling Image - IMAGE: ${image}"
        docker pull $image > /dev/null 2>&1
    else
        echo "> Image already exist locally - Image: ${image}"
    fi
}

function remove_image {

    image=$1
    
    docker image inspect $image > /dev/null 2>&1

    # Remove image if they exist
    if [[ $? -eq 0 ]]; then
        echo "> Removing Image - Image: ${image}"
        docker rmi -f $image > /dev/null 2>&1
    else
        echo "> Image already removed - Image: ${image}"
    fi
}

function build_image {
    # Build an image given a path (Different from pulling a container)

    image=$1
    image_path=$2

    docker image inspect $image > /dev/null 2>&1

    if [[ $? -eq 1 ]]; then
        echo "========== BUILDING IMAGE - ${image}, ${image_path} =========="
        docker build -t $image $image_path
    else
        echo "> Image already built - ${image}, ${image_path}"
    fi
    
}

function show_config {
    # Shows the configuration values currently set
    echo ">> Todo <<"
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
            --name $container_name $image_name > /dev/null 2>&1
    fi

    sleep 2 # Buffer to let it start up internally
}