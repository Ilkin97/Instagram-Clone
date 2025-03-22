#!/bin/bash

echo "Migrating database"

python manage.py migrate

if [ $? -eq 0 ]; then
    echo "Database migrated successfully"
else
    echo "Error migrating database"
fi