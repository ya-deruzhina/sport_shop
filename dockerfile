FROM python:3.10


ENV VAR1=10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code



# Install python dependencies in /.venv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv 
RUN pipenv install


COPY . /code

# Accept a build argument for the container name
#ARG CONTAINER_NAME
#ENV CONTAINER_NAME=$CONTAINER_NAME
# COPY .env ./
RUN > .env
RUN chmod a+x /code/entrypoint.sh
ENTRYPOINT ["/bin/sh", "/code/entrypoint.sh"]