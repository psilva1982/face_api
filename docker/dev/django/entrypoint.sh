#!/bin/bash

# Patch to make the migration automatic for the demo env that will be rebuilt every time
python src/manage.py makemigrations
python src/manage.py migrate

# Start local server
python src/manage.py runserver 0.0.0.0:8000
