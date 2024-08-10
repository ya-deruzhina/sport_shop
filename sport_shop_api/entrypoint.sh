#!/bin/bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate 
pipenv run seed all
pipenv run python manage.py runserver 0.0.0.0:8000
exit

