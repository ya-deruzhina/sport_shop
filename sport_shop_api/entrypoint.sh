#!/bin/bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py runserver
exit

