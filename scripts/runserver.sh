#!/bin/bash

echo "Running server"

python manage.py runserver

if [ $? -eq 0 ]; then
    echo "Server running successfully"
else
    echo "Error running server"
fi