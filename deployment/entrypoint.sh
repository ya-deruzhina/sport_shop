#!/bin/bash

if [ "$@" == "backend" ]; then
  figlet -ct  "Run migrations"
  pipenv run migrate

  figlet -ct  "Run seeds"
  pipenv run seeds

  figlet -ct "Run app server"
  pipenv run server
  #  exec gunicorn api:fast_api --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --timeout 600
fi

if [ "$@" == "celery" ]; then
  figlet -ct "Run celery"
  export C_FORCE_ROOT="true"
  pipenv run celery_app
fi

if [ "$@" == "admin" ]; then
  figlet -ct "Run admin"
  export C_FORCE_ROOT="true"
  pipenv run admin
fi

if [ "$@" == "debug" ]; then
    echo "debug mode On"
    while :; do sleep 10; done
fi

echo "service not found, patch deploy to debug mode"
exit
