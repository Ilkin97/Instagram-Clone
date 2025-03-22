#!/bin/bash

echo "Hello, World!"

python manage.py test

if [ $? -eq 0 ]; then
    echo "Tests passed"
else
    echo "Tests failed"
fi