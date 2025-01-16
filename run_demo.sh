#!/bin/bash

# New Running System: Encompasses testing, live deving and production setup all under one roof

# Usage: ./run.sh <RUN_OPTION> 



# vvvvvvvvvvvvvvvvvvvv CONFIGURATION vvvvvvvvvvvvvvvvvvvv

PROJECT_NAME="Spenny"
LOCAL_PROJECT_PATH=/home/hcheong/projects/spenny

SPENNY_DB_USER="spenny_user"
SPENNY_DB_PASS="spenny_pwd"
SPENNY_DB_NAME="spenny_test_database"
SPENNY_DB_HOST="localhost"
SPENNY_DB_PORT="7777"
SPENNY_DB_SQL_DUMP_FILE_PATH=""
SPENNY_DB_SQL_DUMP_SCHEMA_ONLY=0
SPENNY_DB_CONTAINER_NAME="spenny_test_database_cont"
SPENNY_DB_IMAGE_NAME="postgres:14.5"
SPENNY_DB_TIMEZONE="Australia/Sydney"

BACKEND_PORT=9999
BACKEND_APP_PATH="${LOCAL_PROJECT_PATH}/backend"
BACKEND_CONTAINER_URL="http://localhost:${BACKEND_PORT}"
BACKEND_CONTAINER_NAME="spenny_test_backend_cont"
BACKEND_IMAGE_NAME="spenny_test_backend_img"
BACKEND_TIMEZONE="Australia/Sydney"

BACKEND_CONFIG_PATH=""
BACKEND_LOG_PATH=""
BACKEND_ENV="${LOCAL_PROJECT_PATH}/backend/.venv"

FRONTEND_PORT=8888
FRONTEND_APP_PATH="${LOCAL_PROJECT_PATH}/frontend"
FRONTEND_CONTAINER_URL="http://10.1.50.133:${FRONTEND_PORT}"
FRONTEND_CONTAINER_NAME="airsig_sms_webapp_frontend_cont"
FRONTEND_IMAGE_NAME="airsig_sms_webapp_frontend_img"
FRONTNED_TIMEZONE="Australia/Sydney"

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

source "${LOCAL_PROJECT_PATH}/utils/pg_container_utils.sh"
source "${LOCAL_PROJECT_PATH}/utils/container_utils.sh"

function show_config {
    # Shows the configuration values currently set (SET EVERY TIME)

    echo "PROJECT_NAME: ${PROJECT_NAME}"
    echo "LOCAL_PROJECT_PATH: ${LOCAL_PROJECT_PATH}"
    echo "=============================="
    echo "SPENNY_DB_USER: ${SPENNY_DB_USER}"
    echo "SPENNY_DB_PASS: ${SPENNY_DB_PASS}"
    echo "SPENNY_DB_NAME: ${SPENNY_DB_NAME}"
    echo "SPENNY_DB_HOST: ${SPENNY_DB_HOST}"
    echo "SPENNY_DB_PORT: ${SPENNY_DB_PORT}"
    echo "SPENNY_DB_SQL_DUMP_FILE_PATH: ${SPENNY_DB_SQL_DUMP_FILE_PATH}"
    echo "SPENNY_DB_SQL_DUMP_SCHEMA_ONLY: ${SPENNY_DB_SQL_DUMP_SCHEMA_ONLY}"
    echo "SPENNY_DB_CONTAINER_NAME: ${SPENNY_DB_CONTAINER_NAME}"
    echo "SPENNY_DB_IMAGE_NAME: ${SPENNY_DB_IMAGE_NAME}"
    echo "SPENNY_DB_TIMEZONE: ${SPENNY_DB_TIMEZONE}"
    echo "=============================="
    echo "BACKEND_PORT: ${BACKEND_PORT}"
    echo "BACKEND_APP_PATH: ${BACKEND_APP_PATH}"
    echo "BACKEND_CONTAINER_URL: ${BACKEND_CONTAINER_URL}"
    echo "BACKEND_CONTAINER_NAME: ${BACKEND_CONTAINER_NAME}"
    echo "BACKEND_IMAGE_NAME: ${BACKEND_IMAGE_NAME}"
    echo "BACKEND_TIMEZONE: ${BACKEND_TIMEZONE}"
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

function run_backend {
    # Runs the backend container (CHANGE REQUIRED PER PROJECT)

    docker run -p ${BACKEND_PORT}:8000 \
        -d \
        -e "SPENNY_DB_USER=${SPENNY_DB_USER}" \
        -e "SPENNY_DB_PASS=${SPENNY_DB_PASS}" \
        -e "SPENNY_DB_NAME=${SPENNY_DB_NAME}" \
        -e "SPENNY_DB_HOST=${SPENNY_DB_HOST}" \
        -e "SPENNY_DB_PORT=${SPENNY_DB_PORT}" \
        -e "TZ=${BACKEND_TIMEZONE}" \
        --mount type=bind,source="${BACKEND_APP_PATH}/app",target=/app/ \
        --name ${BACKEND_CONTAINER_NAME} ${BACKEND_IMAGE_NAME}
}

function run_frontend {
    # Runs the Frontend container (CHANGE REQUIRED PER PROJECT)

    docker run -p ${FRONTEND_PORT}:3000 \
        -d \
        -e "BACKEND_CONTAINER_URL=${BACKEND_CONTAINER_URL}" \
        -e "TZ=${FRONTEND_TIMEZONE}" \
        --mount type=bind,source="${FRONTEND_APP_PATH}",target=/app/ \
        --name ${FRONTEND_CONTAINER_NAME} ${FRONTEND_IMAGE_NAME}
}

function set_env_locally {
    # Sets all the required environment but locally (CHANGE REQUIRED PER PROJECT)

    export SPENNY_DB_USER=${SPENNY_DB_USER}
    export SPENNY_DB_PASS=${SPENNY_DB_PASS}
    export SPENNY_DB_NAME=${SPENNY_DB_NAME}
    export SPENNY_DB_HOST=${SPENNY_DB_HOST}
    export SPENNY_DB_PORT=${SPENNY_DB_PORT}

    export TZ=${BACKEND_TIMEZONE}
}

function run_unit_test {

    # Scripts to run unit tests (CHANGE REQUIRED PER PROJECT)

    # Get to the required root directory
    cd /home/hcheong/projects/spenny/backend/
    
    # Activate the appropriate env
    source "${BACKEND_ENV}/bin/activate"

    # Set the Environment Variables
    set_env_locally

}

run_option=$1

if [[ $run_option == "unit" ]]; then
    
    # Running all unit tests
    echo "========== RUNNING UNIT TESTS ($PROJECT_NAME) =========="

    # Tear down any existing DB container (ignore image)
    remove_containers $SMS_CONTAINER_NAME
    remove_containers $AIRSIG_CONTAINER_NAME

    # Spin up DB container (Pull image if it does not exist)
    run_pg_container $SMS_POSTGRES_DB_USER $SMS_POSTGRES_DB_PASS $SMS_POSTGRES_DB_NAME $SMS_POSTGRES_DB_HOST $SMS_POSTGRES_DB_PORT $SMS_CONTAINER_NAME $SMS_IMAGE_NAME $SMS_TIMEZONE
    run_pg_container $AIRSIG_POSTGRES_DB_USER $AIRSIG_POSTGRES_DB_PASS $AIRSIG_POSTGRES_DB_NAME $AIRSIG_POSTGRES_DB_HOST $AIRSIG_POSTGRES_DB_PORT $AIRSIG_CONTAINER_NAME $AIRSIG_IMAGE_NAME $AIRSIG_TIMEZONE

    # Run Tests
    run_unit_test

    # Tear down any container (ignore image)
    remove_containers $SMS_CONTAINER_NAME
    remove_containers $AIRSIG_CONTAINER_NAME
fi

if [[ $run_option == "demo" ]]; then
    # Running a live demo with sample data
    echo "========== RUNNING DEMO MODE ($PROJECT_NAME) =========="

    # Pull Image
    pull_image $SMS_IMAGE_NAME

    # Tear down any existing DB container (ignore image)
    remove_containers $SMS_CONTAINER_NAME

    # Spin up DB container (Pull image if it does not exist)
    run_pg_container $SMS_POSTGRES_DB_USER $SMS_POSTGRES_DB_PASS $SMS_POSTGRES_DB_NAME $SMS_POSTGRES_DB_HOST $SMS_POSTGRES_DB_PORT $SMS_CONTAINER_NAME $SMS_IMAGE_NAME $SMS_TIMEZONE
    load_pg_dump_file $SMS_POSTGRES_DB_USER $SMS_POSTGRES_DB_PASS $SMS_POSTGRES_DB_NAME $SMS_POSTGRES_DB_HOST $SMS_POSTGRES_DB_PORT $SMS_SQL_DUMP_FILE_PATH
    clear_content_pg_file $SMS_POSTGRES_DB_USER $SMS_POSTGRES_DB_PASS $SMS_POSTGRES_DB_NAME $SMS_POSTGRES_DB_HOST $SMS_POSTGRES_DB_PORT $SMS_SQL_DUMP_SCHEMA_ONLY

    # Tear down Application Containers
    remove_containers $BACKEND_CONTAINER_NAME
    remove_containers $FRONTEND_CONTAINER_NAME

    # Build Application Containers
    build_image $BACKEND_IMAGE_NAME $BACKEND_APP_PATH
    build_image $FRONTEND_IMAGE_NAME $FRONTEND_APP_PATH

    # Spin up Frontend Container
    run_backend

    # Spin up Backend Container
    run_frontend

    sleep 1

    # Show the container statuses
    show_container_status

    # Show Container Links
    show_container_url $BACKEND_CONTAINER_URL $BACKEND_CONTAINER_NAME
    show_container_url $FRONTEND_CONTAINER_URL $FRONTEND_CONTAINER_NAME

    # Show DB Access
    show_pg_access_cmd $SMS_POSTGRES_DB_USER $SMS_POSTGRES_DB_PASS $SMS_POSTGRES_DB_NAME $SMS_POSTGRES_DB_HOST $SMS_POSTGRES_DB_PORT $SMS_CONTAINER_NAME
    show_pg_access_cmd $AIRSIG_POSTGRES_DB_USER $AIRSIG_POSTGRES_DB_PASS $AIRSIG_POSTGRES_DB_NAME $AIRSIG_POSTGRES_DB_HOST $AIRSIG_POSTGRES_DB_PORT $AIRSIG_CONTAINER_NAME
fi

if [[ $run_option == "stop" ]]; then 
    # Stop and remove all containers
    exit 1
fi

if [[ $run_option == "clean" ]]; then 
    # Stop and remove all containers and image
    remove_containers $SMS_CONTAINER_NAME
    remove_containers $AIRSIG_CONTAINER_NAME

    remove_containers $BACKEND_CONTAINER_NAME
    remove_containers $FRONTEND_CONTAINER_NAME
    
    remove_image $SMS_IMAGE_NAME
    remove_image $AIRSIG_IMAGE_NAME
fi

if [[ $run_option == "help" ]]; then
    # Show Usage
    echo "========== USAGE =========="
    echo "> ./run.sh unit - Builds the environment and runs unit tests. Resets any databases"
    echo "> ./run.sh demo - Builds the environment and runs demo/dev. Resets any databases"
    echo "> ./run.sh stop - Stops and remove all running containers. Resets any databases"
    echo "> ./run.sh clean - Stop and remove all containers AND images. Clears any databases"
    echo "> ./run.sh help - Shows all the possible options"
fi