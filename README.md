# Spenny

Spenny is a basic webapp built to better track and monitor ones spending by being able to automate as well as organise your money into discrete buckets.

Is it useful? Well it is for me

## Running - LOCALLY

Adjustments need to be made to the port in the config.js

### Backend

Assuming that you have never installed dependencies, run the follow command
Enter the `/backend/app`

```
pip install -r requirements.txt &&
pip install 'fastapi[all]' SQLalchemy
```

To run the application run the following command

```
python3 -m uvicorn main:app
```

The application defaults to port 8000

### Frontend

Assuming that you have never installed dependencies, run the follow command
Enter the `/frontend/`

```
yarn install
```

To run the application run the following command

```
yarn start
```

The application defaults to port 3000

## Running - DOCKERISE

The application also runs as 2 different docker containers and scripts are provided to run them

### Building the images

To build the necessary environment images, run the following command

```
sh build_startup.sh
```

### Running the container

Prior to running the container, you do need to firstly install node_modules in the `/frontend/`, run the following command
```
yarn install
```

Once the node modules have been installed, run the following script to start the container

```
sh run_startup.sh
```