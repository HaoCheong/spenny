#!/usr/bin/bash

run_option=$1
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
local_path="/home/hcheong/projects/spenny"
=======
local_path="/home/hcheong/Desktop/Other/spenny"
>>>>>>> 23f32d9 (Fixed the event schemas and response and create to ensure it works as intended)
=======
local_path="/home/hcheong/projects/spenny"
>>>>>>> a5b6c15 (Updated env to the local path + docker compose pathing)
=======
local_path="/home/hcheong/Desktop/Other/spenny"
>>>>>>> 83804f9 (Add a timeframe get endpoint for events)
=======
local_path="/home/hcheong/Desktop/Other/SIDE_PROJECTS/spenny"
>>>>>>> 6ce8c49 (Updated all buttons to have its own rounding, started the EventRow for view)

if [[ $run_option == "demo" ]]; then
    set -a && source demo.env && set +a
    docker compose --progress=plain build --no-cache 
    docker compose --env-file $local_path/demo.env -f docker-compose.yml --profile demo up --force-recreate --remove-orphans --renew-anon-volumes -d
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "FRONTEND URL -> $FRONTEND_CONTAINER_URL"
<<<<<<< HEAD
=======
local_path="/home/hcheong/Desktop/Other/spenny"
=======
local_path="/home/hcheong/projects/spenny"
>>>>>>> f53ba7f (Updated the DB and updated the buckets model and schema to include bucket type)

if [[ $run_option == "demo" ]]; then
    source demo.env
=======
local_path="/home/hcheong/Desktop/Other/spenny"
=======
local_path="/home/hcheong/projects/spenny"
>>>>>>> b2d335e (Moved testing to its own docker compose)

if [[ $run_option == "demo" ]]; then
    set -a && source demo.env && set +a
<<<<<<< HEAD
    # docker compose build --no-cache
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2e77600 (Fixed up docker file and begin writing bucket execution)
    docker compose --env-file $local_path/demo.env up --force-recreate --remove-orphans --renew-anon-volumes -d
=======
    docker compose --env-file $local_path/demo.env -f docker-compose.yml up --force-recreate --remove-orphans --renew-anon-volumes -d
>>>>>>> b2d335e (Moved testing to its own docker compose)
=======
=======
    docker compose build --no-cache
>>>>>>> 4433b67 (Investigating logging all read pydantic error)
    docker compose --env-file $local_path/demo.env -f docker-compose.yml --profile demo up --force-recreate --remove-orphans --renew-anon-volumes -d
>>>>>>> 92e98b1 (Added profiles for startup and added new test env)
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
>>>>>>> 69fca77 (Added run script)
=======
>>>>>>> de9f843 (Added tailwind and dockerised the frontend)
    echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

if [[ $run_option == "live" ]]; then
<<<<<<< HEAD
<<<<<<< HEAD
    set -a && source live.env && set +a
    docker compose build --no-cache
<<<<<<< HEAD
<<<<<<< HEAD
    docker compose --env-file $local_path/live.env -f docker-compose.yml --profile live up --force-recreate --remove-orphans --renew-anon-volumes -d
=======
    source live.env
<<<<<<< HEAD
<<<<<<< HEAD
    docker compose --env-file `$local_path/live.env` up --force-recreate --remove-orphans -d
>>>>>>> 69fca77 (Added run script)
=======
    docker compose --env-file $local_path/live.env up --force-recreate --remove-orphans -d
>>>>>>> 79d3c0a (Updated run sh pathing)
=======
=======
    set -a && source live.env && set +a
    docker compose build --no-cache
>>>>>>> 2e77600 (Fixed up docker file and begin writing bucket execution)
    docker compose --env-file $local_path/live.env up --force-recreate --remove-orphans --renew-anon-volumes -d
>>>>>>> f53ba7f (Updated the DB and updated the buckets model and schema to include bucket type)
=======
    docker compose --env-file $local_path/live.env -f docker-compose.yml up --force-recreate --remove-orphans --renew-anon-volumes -d
>>>>>>> b2d335e (Moved testing to its own docker compose)
=======
    docker compose --env-file $local_path/live.env -f docker-compose.yml --profile live up --force-recreate --remove-orphans --renew-anon-volumes -d
>>>>>>> 92e98b1 (Added profiles for startup and added new test env)
    echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
    echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
    echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
    echo "================================== END =================================="
    exit 0
fi

<<<<<<< HEAD
<<<<<<< HEAD
if [[ $run_option == "unit" ]]; then
    set -a && source demo.env && set +a
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

echo "USAGE: ./run.sh [demo|live|unit|stop]"
=======
=======
if [[ $run_option == "unit" ]]; then
    set -a && source demo.env && set +a
    docker compose build --no-cache
    docker compose --env-file $local_path/test.env -f docker-compose.yml --profile test up --force-recreate --remove-orphans --renew-anon-volumes -d
    sleep 2
    cd backend
    python3 -m pytest $local_path/backend/tests/unit/bucket_tests.py
    python3 -m pytest $local_path/backend/tests/unit/event_tests.py
    python3 -m pytest $local_path/backend/tests/unit/log_tests.py
fi

>>>>>>> b2d335e (Moved testing to its own docker compose)
if [[ $run_option == "stop" ]]; then

    docker compose --env-file $local_path/demo.env stop 
    docker compose --env-file $local_path/demo.env down --volumes --remove-orphans

    docker compose --env-file $local_path/live.env stop 
    docker compose --env-file $local_path/live.env down --volumes --remove-orphans
    exit 0
fi

<<<<<<< HEAD
echo "USAGE: ./run.sh [demo|live|stop]"
>>>>>>> 69fca77 (Added run script)
=======
echo "USAGE: ./run.sh [demo|live|unit|stop]"
>>>>>>> 4433b67 (Investigating logging all read pydantic error)
