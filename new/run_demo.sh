#!/bin/bash

# New Running System: Encompasses testing, live deving and production setup all under one roof

# Usage: ./run.sh <RUN_OPTION> 

# vvvvvvvvvvvvvvvvvvvv CONFIGURATION vvvvvvvvvvvvvvvvvvvv

PROJECT_NAME="Spenny v1.1 Demo"
LOCAL_PROJECT_PATH="/home/hcheong/Desktop/Other/spenny/new"

SPENNY_POSTGRES_DB_USER="spenny_demo_db_user"
SPENNY_POSTGRES_DB_PASS="spenny_demo_db_pass"
SPENNY_POSTGRES_DB_NAME="spenny_demo_db"
SPENNY_POSTGRES_DB_HOST="10.1.50.133"
SPENNY_POSTGRES_DB_PORT="8681"
SPENNY_SQL_DUMP_FILE_PATH=""
SPENNY_SQL_DUMP_SCHEMA_ONLY=0
SPENNY_CONTAINER_NAME="spenny_demo_db_cont"
SPENNY_IMAGE_NAME="postgres:14.5"
SPENNY_TIMEZONE="Australia/Sydney"

BACKEND_PORT=8682
BACKEND_APP_PATH="${LOCAL_PROJECT_PATH}/backend"
BACKEND_CONTAINER_URL="http://${SPENNY_POSTGRES_DB_HOST}:${BACKEND_PORT}"
BACKEND_CONTAINER_NAME="spenny_demo_backend_cont"
BACKEND_IMAGE_NAME="spenny_demo_backend_img"
BACKEND_TIMEZONE="Australia/Sydney"
BACKEND_DOCKER_PATH="${LOCAL_PROJECT_PATH}/backend/Dockerfile"

BACKEND_ENV="${LOCAL_PROJECT_PATH}/.venv"

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# /home/hcheong/projects/spenny/new/utils/container_utils.sh
source "${LOCAL_PROJECT_PATH}/utils/container_utils.sh"
source "${LOCAL_PROJECT_PATH}/utils/pg_container_utils.sh"

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

function run_backend {
    # Runs the backend container (CHANGE REQUIRED PER PROJECT)

    docker run -p ${BACKEND_PORT}:8000 \
        -d \
        -e "SPENNY_POSTGRES_DB_USER=${SPENNY_POSTGRES_DB_USER}" \
        -e "SPENNY_POSTGRES_DB_PASS=${SPENNY_POSTGRES_DB_PASS}" \
        -e "SPENNY_POSTGRES_DB_NAME=${SPENNY_POSTGRES_DB_NAME}" \
        -e "SPENNY_POSTGRES_DB_HOST=${SPENNY_POSTGRES_DB_HOST}" \
        -e "SPENNY_POSTGRES_DB_PORT=${SPENNY_POSTGRES_DB_PORT}" \
        -e "TZ=${BACKEND_TIMEZONE}" \
        --mount type=bind,source="${BACKEND_APP_PATH}/app",target=/app/ \
        --name ${BACKEND_CONTAINER_NAME} ${BACKEND_IMAGE_NAME}
}

function set_env_locally {
    # Sets all the required environment but locally (CHANGE REQUIRED PER PROJECT)

    export SPENNY_POSTGRES_DB_USER=${SPENNY_POSTGRES_DB_USER}
    export SPENNY_POSTGRES_DB_PASS=${SPENNY_POSTGRES_DB_PASS}
    export SPENNY_POSTGRES_DB_NAME=${SPENNY_POSTGRES_DB_NAME}
    export SPENNY_POSTGRES_DB_HOST=${SPENNY_POSTGRES_DB_HOST}
    export SPENNY_POSTGRES_DB_PORT=${SPENNY_POSTGRES_DB_PORT}
    export TZ=${BACKEND_TIMEZONE}
}

function run_unit_test {

    # Scripts to run unit tests (CHANGE REQUIRED PER PROJECT)

    # Get to the required root directory
    cd "${LOCAL_PROJECT_PATH}"
    
    # Activate the appropriate env
    source "${BACKEND_ENV}/bin/activate"

    # Set the Environment Variables
    set_env_locally

    echo ">>> TODO <<<"
}


run_option=$1

if [[ $run_option == "unit" ]]; then
    
    # Running all unit tests
    echo "========== RUNNING UNIT TESTS ($PROJECT_NAME) =========="

    # Pull Image
    pull_image postgres:14.5

    # Tear down any existing DB container (ignore image)
    remove_containers $SPENNY_CONTAINER_NAME

    # Spin up DB container (Pull image if it does not exist)
    run_pg_container $SPENNY_POSTGRES_DB_USER $SPENNY_POSTGRES_DB_PASS $SPENNY_POSTGRES_DB_NAME $SPENNY_POSTGRES_DB_HOST $SPENNY_POSTGRES_DB_PORT $SPENNY_CONTAINER_NAME $SPENNY_IMAGE_NAME $SPENNY_TIMEZONE

    # Run Tests
    run_unit_test

    # Tear down any container (ignore image)
    remove_containers $SPENNY_CONTAINER_NAME
fi

if [[ $run_option == "demo" ]]; then
    # Running a live demo with sample data
    echo "========== RUNNING DEMO MODE ($PROJECT_NAME) =========="

    # Pull Image
    pull_image $SPENNY_IMAGE_NAME

    # Tear down any existing DB container (ignore image)
    remove_containers $SPENNY_CONTAINER_NAME

    # Spin up DB container (Pull image if it does not exist)
    run_pg_container $SPENNY_POSTGRES_DB_USER $SPENNY_POSTGRES_DB_PASS $SPENNY_POSTGRES_DB_NAME $SPENNY_POSTGRES_DB_HOST $SPENNY_POSTGRES_DB_PORT $SPENNY_CONTAINER_NAME $SPENNY_IMAGE_NAME $SPENNY_TIMEZONE
    load_pg_dump_file $SPENNY_POSTGRES_DB_USER $SPENNY_POSTGRES_DB_PASS $SPENNY_POSTGRES_DB_NAME $SPENNY_POSTGRES_DB_HOST $SPENNY_POSTGRES_DB_PORT $SPENNY_SQL_DUMP_FILE_PATH
    clear_content_pg_file $SPENNY_POSTGRES_DB_USER $SPENNY_POSTGRES_DB_PASS $SPENNY_POSTGRES_DB_NAME $SPENNY_POSTGRES_DB_HOST $SPENNY_POSTGRES_DB_PORT $SPENNY_SQL_DUMP_SCHEMA_ONLY

    # Tear down Application Containers
    remove_containers $BACKEND_CONTAINER_NAME

    # Build Application Containers
    build_image $BACKEND_IMAGE_NAME $BACKEND_APP_PATH $BACKEND_DOCKER_PATH

    # Spin up Frontend Container
    run_backend

    sleep 1

    # Show the container statuses
    show_container_status

    # Show Container Links
    show_container_url $BACKEND_CONTAINER_URL $BACKEND_CONTAINER_NAME

    # Show DB Access
    show_pg_access_cmd $SPENNY_POSTGRES_DB_USER $SPENNY_POSTGRES_DB_PASS $SPENNY_POSTGRES_DB_NAME $SPENNY_POSTGRES_DB_HOST $SPENNY_POSTGRES_DB_PORT $SPENNY_CONTAINER_NAME
fi

if [[ $run_option == "stop" ]]; then

    # Stop and remove all containers
    remove_containers $SPENNY_CONTAINER_NAME
    remove_containers $BACKEND_CONTAINER_NAME

    exit 1
fi

if [[ $run_option == "build" ]]; then 
    # Stop and remove all containers (CHANGE REQUIRED PER PROJECT)
    
    build_image $BACKEND_IMAGE_NAME $BACKEND_APP_PATH
fi

if [[ $run_option == "clean" ]]; then 
    # Stop and remove all containers and image
    remove_containers $SPENNY_CONTAINER_NAME

    remove_containers $BACKEND_CONTAINER_NAME
    
    remove_image $SPENNY_IMAGE_NAME

    remove_image $BACKEND_IMAGE_NAME
fi

if [[ $run_option == "help" ]]; then
    # Show Usage
    echo "========== USAGE =========="
    echo "> ./run.sh build - Build and required containers"
    echo "> ./run.sh unit - Builds the environment and runs unit tests. Resets any databases"
    echo "> ./run.sh demo - Builds the environment and runs demo/dev. Resets any databases"
    echo "> ./run.sh stop - Stops and remove all running containers. Resets any databases"
    echo "> ./run.sh clean - Stop and remove all containers AND images. Clears any databases"
    echo "> ./run.sh help - Shows all the possible options"
fi
