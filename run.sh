#!/usr/bin/bash

run_option=$1
local_path="/home/hcheong/Desktop/Other/spenny"

if [[ $run_option == "demo" ]]; then
    set -a && source demo.env && set +a
    # docker compose build --no-cache
    docker compose --env-file $local_path/demo.env -f docker-compose.yml up --force-recreate --remove-orphans --renew-anon-volumes -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "live" ]]; then
    set -a && source live.env && set +a
    docker compose build --no-cache
    docker compose --env-file $local_path/live.env -f docker-compose.yml up --force-recreate --remove-orphans --renew-anon-volumes -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "unit" ]]; then
    set -a && source demo.env && set +a
    # docker compose build --no-cache
    docker compose -f docker-compose-test.yml up --force-recreate --remove-orphans --renew-anon-volumes -d
    sleep 1
    cd backend
    python3 -m pytest --disable-warnings $local_path/backend/tests/unit/bucket_tests.py
    python3 -m pytest --disable-warnings $local_path/backend/tests/unit/event_tests.py
fi

if [[ $run_option == "stop" ]]; then

    docker compose --env-file $local_path/demo.env stop 
    docker compose --env-file $local_path/demo.env down --volumes --remove-orphans

    docker compose --env-file $local_path/live.env stop 
    docker compose --env-file $local_path/live.env down --volumes --remove-orphans
    exit 0
fi

echo "USAGE: ./run.sh [demo|live|stop]"