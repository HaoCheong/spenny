#!/usr/bin/bash

run_option=$1
local_path="/home/hcheong/projects/spenny/env"

if [[ $run_option == "demo" ]]; then
    set -a && source env/demo.env && set +a
    docker compose --progress=plain build --no-cache 
    docker compose --env-file $local_path/demo.env -f docker-compose.yml --profile demo up --force-recreate --remove-orphans --renew-anon-volumes -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "FRONTEND URL -> $FRONTEND_CONTAINER_URL"
fi

# if [[ $run_option == "demo" ]]; then
#     set -a && source env/demo.env && set +a

#     docker compose --env-file $local_path/demo.env -f docker-compose.yml up --force-recreate --remove-orphans --renew-anon-volumes -d
#     docker compose build --no-cache

#     echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
#     echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
#     echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
#     echo "================================== END =================================="
#     exit 0
# fi

if [[ $run_option == "live" ]]; then

    set -a && source env/live.env && set +a
    docker compose build --no-cache
    docker compose --env-file $local_path/live.env -f docker-compose.yml --profile live up --force-recreate --remove-orphans --renew-anon-volumes -d
    docker compose --env-file `$local_path/live.env` up --force-recreate --remove-orphans -d

    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "unit" ]]; then
    set -a && source env/demo.env && set +a
    docker compose build --no-cache
    docker compose --env-file $local_path/test.env -f docker-compose.yml --profile test up --force-recreate --remove-orphans --renew-anon-volumes -d
    sleep 2
    cd backend
    python3 -m pytest $local_path/backend/tests/unit/bucket_tests.py
    python3 -m pytest $local_path/backend/tests/unit/event_tests.py
    python3 -m pytest $local_path/backend/tests/unit/log_tests.py
fi

if [[ $run_option == "stop" ]]; then

    docker compose --env-file $local_path/demo.env stop 
    docker compose --env-file $local_path/demo.env down --volumes --remove-orphans

    docker compose --env-file $local_path/live.env stop 
    docker compose --env-file $local_path/live.env down --volumes --remove-orphans

    docker compose --env-file $local_path/test.env stop 
    docker compose --env-file $local_path/test.env down --volumes --remove-orphans
    exit 0
fi
s
echo "USAGE: ./run.sh [demo|live|unit|stop]"

