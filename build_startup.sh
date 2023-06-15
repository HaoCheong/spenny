#!/bin/bash

# Check if backend image exist (if so, delete)
if /usr/bin/docker image inspect spenny_backend > /dev/null 2>&1; then
    echo "Removing spenny backend"
    /usr/bin/docker image rmi spenny_backend > /dev/null
fi

if /usr/bin/docker image inspect spenny_frontend > /dev/null 2>&1; then
    echo "Removing spenny frontend"
    /usr/bin/docker image rmi spenny_frontend > /dev/null
fi

/usr/bin/docker build -t "spenny_backend" ./backend
/usr/bin/docker build -t "spenny_frontend" ./frontend
