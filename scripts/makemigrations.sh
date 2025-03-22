#!/bin/bash

echo "Making migrations"

python manage.py makemigrations

if [ $? -eq 0 ]; then
    echo "Migrations created successfully"
else
    echo "Error creating migrations"
fi