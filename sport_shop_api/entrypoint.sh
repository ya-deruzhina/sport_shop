#!/bin/bash
pipenv run python manage.py migrate 
pipenv run python manage.py runserver 0.0.0.0:8000
pipenv run celery -A sport_shop_api worker -l INFO
exit

