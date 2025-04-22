# Spenny v1.1.0


## Changelog

Date: Mon 17 Jan 2025
### Features
- Flow events can now be edited
- Flow events can now be deleted
- Bucket can now be edited
- Bucket can now be deleted
- Triggering the flow events will now occur on every refresh of the page. Run update button no longer needed
- Bring Forward Trigger for Flow Events
	- Allows user to update trigger date by how ever long they have set the frequency of the update
	- Update trigger can also include the relevant money flow event. Allow users to pre-maturely trigger an event while maintaining frequency consistency.


## Overview

Spenny is a basic web application built to better track and monitor ones spending by being able to automate as well as organize your money into discrete buckets.

Conceptually, money is organized into buckets and flow events can be created to automatically transfer, add, and remove money from buckets, mimicking the action of recurring payments. Buckets are representative of how one will allocate money and flow events is the process of that allocation.

Idea is by having a better eye on ones view of the allocation of money, the better one can budget their money to ensure none is wasted.

## Installation

The application is ran completely as docker containers. Docker is a **pre-requisite** to using the application. Two major scripts have been provided that help with the deployment of the containers:
- `./run_demo.sh`: Used for running tests and running demo builds
- `./run_live.sh`: Deploying containers under production configurations

## Configuration

Below are the configuration options that needs to be configured in both prior to usage:

| Configuration Option           | Description                                                           | Example                                 | Required for Production |
| ------------------------------ | --------------------------------------------------------------------- | --------------------------------------- | ----------------------- |
| LOCAL_PROJECT_PATH             | The path where the root project directory is located                  | /path/to/project/                       | YES                     |
| SPENNY_DB_USER                 | The PostgreSQL user of the database to use                            | spenny_db_user                          | YES                     |
| SPENNY_DB_PASS                 | The PostgreSQL password of the database to use                        | password123!                            | YES                     |
| SPENNY_DB_NAME                 | The PostgreSQL database name to use                                   | spenny_db                               | YES                     |
| SPENNY_DB_HOST                 | The PostgreSQL host IP of the database to use                         | 10.10.10.10                             | YES                     |
| SPENNY_DB_PORT                 | The PostgreSQL port of the database to use                            | 5432                                    | YES                     |
| SPENNY_DB_SQL_DUMP_FILE_PATH   | The absolute path of the DUMP file to use                             | /path/to/dump_file/dump.sql             | NO                      |
| SPENNY_DB_SQL_DUMP_SCHEMA_ONLY | Flag for whether you are keeping the the data of the dump file or not | 1                                       | NO                      |
| SPENNY_DB_CONTAINER_NAME       | The container name of the PostgreSQL Database                         | spenny_db_cont                          | NO                      |
| SPENNY_DB_IMAGE_NAME           | The image name of the PostgreSQL Database                             | spenny_db_img                           | NO                      |
| SPENNY_DB_TIMEZONE             | The local timezone of the PostgreSQL Database container               | Australia/Sydney                        | NO                      |
| BACKEND_PORT                   | The expose port of the backend container                              | 9999                                    | YES                     |
| BACKEND_APP_PATH               | The path to the backend folder                                        | /path/to/project/backend                | YES                     |
| BACKEND_CONTAINER_URL          | The backend container URL that will be used                           | http://10.10.10.10:8888/                | YES                     |
| BACKEND_CONTAINER_NAME         | The container name for the backend                                    | spenny_be_cont                          | YES                     |
| BACKEND_IMAGE_NAME             | The image name for the backend                                        | spenny_be_img                           | YES                     |
| BACKEND_TIMEZONE               | The local timezone of the backend container                           | Australia/Sydney                        | YES                     |
| BACKEND_CONFIG_PATH            | The path to the backend configuration file                            | /path/to/project/config/spenny_conf.yml | YES                     |
| BACKEND_LOG_PATH               | The path to the backend configuration log                             | /path/to/project/log/spenny.log         | YES                     |
| BACKEND_ENV                    | The path to the backend virtual environment                           | /path/to/project/backend/.venv          | NO                      |
| FRONTEND_PORT                  | The expose port of the frontend container                             | 8888                                    | YES                     |
| FRONTEND_APP_PATH              | The path to the frontend folder                                       | /path/to/project/frontend               | YES                     |
| FRONTEND_CONTAINER_URL         | The frontend container URL that will be used                          | http://10.10.10.10:9999                 | YES                     |
| FRONTEND_CONTAINER_NAME        | The container name for the frontend                                   | spenny_fe_cont                          | YES                     |
| FRONTEND_IMAGE_NAME            | The image name for the frontend                                       | spenny_fe_img                           | YES                     |
| FRONTEND_TIMEZONE              | The local timezone of the frontend container                          | Australia/Sydney                        | YES                     |

## Usage
### Unit Testing

To run the tests to ensure the current code operates accordingly.

First you have to set up a python virtual environment and install the requirements You can run the following commands in your terminal. These only have to be done once:


```bash
# Enter the backend directory
cd backend

# Create the virtual environment
python3 -m venv .venv

# Activate the newly created environment
source activate .venv/bin/activate

# Install all the requirements
pip3 install -r requirements

# Deactivate the environment
source deactivate
```

Then within the `./run_demo.sh` script, update the backend environment field with the environment path

```bash
BACKEND_ENV="path/to/backend/.venv"
```

Once the setup has been done, you can simply run the following command to run unit tests

```bash
./run_demo.sh unit
```

### Demo

A demo setup can be created with perishable docker contained database.

A sample database dump has also been created to be used. Once all the proper configuration is made in `./run_demo.sh` configuration section, simply run the following command:

```bash
./run_demo.sh demo
```

> Demo mode means that any changes done to the application will not persist on the restart of the container.

More commands are available if you run the following command:

```
./run_demo.sh help
```

### Production

A production setup can be created but will not spin up perishable containers (unlike those of demo). Simply set the configuration in `./run_live.sh` and run the following

```bash
./run_live.sh start
```

More commands are available if you run the following command:

```
./run_live.sh help
```

