# Spenny v1.1.0


## Changelog

Date: Mon 15 Apr 2024
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

There are application can be ran as either local docker containers if you want to host the container on a separate server or completely locally. Scripts have also been created to help the process
### Docker

If you have not build the docker image, you can use the following command script found in the project root directory to create both the backend and frontend images.

```bash
./build_startup.sh
```
### Locally

To run the application locally (in development mode), run the following commands.

Run the following commands to install the dependencies required from the project root directory

```bash
# Installing Backend FastAPI Dependency
pip3 install -r backend/app/requirements

# Install Frontend NPM Packages
cd frontend
npm install
```

## Startup

### Docker

Once docker images have been created, you can use the following command script found in the project root directory to run both the backend and frontend containers.

```
./run_startup.sh
```

The run script can also be used to stop the containers:
```
./run_startup.sh stop
```

### Locally

To start the FastAPI backend, run the following command from the `backend` folder.

```bash
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 9991
```

To start the FastAPI backend, run the following command from the `frontend` folder:

```bash
npm start
```

## Testing

Several Testing system and types are provided:
- **Unit Testing** (`backend/tests/unit`): Testing Specific Functions and CRUD features
- **Populate** (`backend/tests/populate`): A auto script that populates the database to provide test data to for future smoke testing

To run the unit tests run the following script in the project root directory

```bashy
./run_tests.sh
```

To run the populate script, while the backend is running (either container or locally), run the following command

```
./tests/populate/populate.py
```
