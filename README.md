# Django REST API

## How to install and run

1. Clone the repository
2. Install requirements with dev requirements via pipenv `pipenv install --dev`. Use
`pipenv install` if dev requirements is not needed.
3. Fill `.env` file based on `.env.example`
4. Activate pipenv environment (if needed) `pipenv shell`
5. Run migrations via `pipenv run migrate`
6. Run seeds `pipenv run seed all`
7. Run API (FastAPI) server by typing `pipenv run server`
The Swagger docs will be accessible on the `/doc` endpoint
8. Run Admin Panel (Flask Admin) server by typing `pipenv run admin`
To log in use credentials from `seeds/admins.py`
9. Run Python Console (IPython) by typing `pipenv run shell`. Main classes will be imported.
10. To use the applicatin in production use gunicorn with Uvicorn. Example of the command:
`pipenv run gunicorn internals.wsgi --workers 4 --bind 0.0.0.0:8003`

## How to work with Django Views
1. Create any route at any hierarchy level inside `apps` folder.
2. Create `urls_{version}.py` file import views. Version is according to the version of API.
For instance, `urls_v1.py`, `urls_v2.py` files.
3. The routers will be automatically imported and added to Django.
Example in `apps/users/urls_v1.py` file.

## Swagger
This project uses JSON Open API description
To add a new endpoint you should create a new file in `swagger/openapi/paths` folder.
Your JSON file will be automatically merged into the total Swagger description.
You can add reusable components into `swagger/openapi/components/index.json` file.
More details are in `swagger/swagger_json_builder.py` file.


## Seeds

"admins" - inits database with default admin.

### Introduction

Seeds are data initialization for models such as `<Model name>`, and etc.
Sctipts are one time scripts

1. Сreate new .py file inside `scripts/seeds` / `scipts/one_time_scripts` folder
2. Write a script and add `perform` method as entrypoint into your script
3. Add filename into `script_names` in `scripts/run_seeds.py` or `scripts/run_script.py` file

### Usage

1. Run script via `pipenv run seed seed_name` / `pipenv run script <args>`
2. To run all seeds `pipenv run seed all`. Scripts has some params thus scipts can be run only by one

### !IMPORTANT

Try to write yout script by using methods `get_or_create` or similar
to avoid duplication in database

#### Provided seeds

- admin - create admin user. NOTE: Don't forget to change admin password after running.
# sport_shop
