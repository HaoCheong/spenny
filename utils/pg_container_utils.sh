#!/bin/bash

####################################################################
########## POSTGRESQL CONTAINER MANAGEMENT UTILITY SCRIPT ##########
####################################################################


function run_pg_container {

    # Spin up a blank container

    db_user=$1
    db_pass=$2
    db_name=$3
    db_host=$4
    db_port=$5

    container_name=$6
    image_name=$7
    timezone=$8

    # Run container
    if docker container inspect $container_name > /dev/null 2>&1; then
        echo "> PostgreSQL Container already running - Container: ${container_name}"
    else
        echo "> Running PostgreSQL Container - Container: ${container_name}"
        docker run\
            -d \
            -e POSTGRES_USER=$db_user\
            -e POSTGRES_PASSWORD=$db_pass\
            -e POSTGRES_DB=$db_name\
            -e TZ=$TIMEZONE\
            -p $db_port:5432\
            --name $container_name $image_name > /dev/null 2>&1
    fi

    sleep 2 # Buffer to let it start up internally
}

function load_pg_dump_file {
    
    # Loads a given dump file

    db_user=$1
    db_pass=$2
    db_name=$3
    db_host=$4
    db_port=$5

    sql_db_file_path=$6

    if [[ ${sql_db_file_path} != "" ]]; then
        echo "========== LOADING SQL DUMP FILE =========="
        echo "> Proceeding to load in PostgreSQL Dump File - Dump File Path: ${sql_db_file_path}"

        $(PGPASSWORD=$db_pass psql -h localhost -p $db_port -d $db_name -U $db_user < "${sql_db_file_path}" > /dev/null 2>&1) 

    fi

}

function clear_content_pg_file {

    db_user=$1
    db_pass=$2
    db_name=$3
    db_host=$4
    db_port=$5

    sql_db_schema_only=$6

    if [[ ${sql_db_schema_only} == 1 ]]; then
        echo "========== CLEARING SQL DUMP FILE =========="

        # Get all tables
        pub_tables=$(PGPASSWORD=$db_pass psql -h localhost -p $db_port -d $db_name -U $db_user -t -c "select table_name from information_schema.tables WHERE table_schema = 'public';")

        # Drop all content
        for tab in $pub_tables; do
            $(PGPASSWORD=$db_pass psql -h localhost -p $db_port -d $db_name -U $db_user -t -c "DELETE FROM $tab CASCADE;" > /dev/null 2>&1)
        done

    fi
}

function show_pg_access_cmd {

    # Shows the access command for PostgreSQL

    db_user=$1
    db_pass=$2
    db_name=$3
    db_host=$4
    db_port=$5

    container_name=$6

    echo "========== ACCESS COMMAND - ${container_name} =========="
    echo "PGPASSWORD=${db_pass} PAGER='less -S' psql -h ${db_host} -p ${db_port} -d ${db_name} -U ${db_user}"
}

function pg_run_db_query {
    
    # Runs a SQL query on an already existing postgreSQL container 

    db_user=$1
    db_pass=$2
    db_name=$3
    db_host=$4
    db_port=$5

    query=$6
    desc=$7

    echo "> $desc"
    $(PGPASSWORD=$db_pass psql -h localhost -p $db_port -d $db_name -U $db_user -t -c "$query" > /dev/null 2>&1)
    
}