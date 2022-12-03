# FastAPI with Django ORM and Admin

## Overview

This is a template repository for implementing the server using Django functionality for the DB area (admin, ORM) and FastAPI for the API area.

## Prerequisites

### Poetry

Dependency management for Python files is done using POETRY.

1. <https://python-poetry.org/docs/#installation>
1. `python -m venv venv`
1. `source venv/bin/activate`
2. `pip install --upgrade pip` (if needed)
3. `poetry install`

### pre-commit (for developers)

This tool defines commands to be executed before committing. It is already defined in `.pre-commit-config.yaml`, so you need to configure it in your environment. Please follow the steps below.

1. <https://pre-commit.com/#installation>
1. `pre-commit install`

## Usage

1. Clone this repository

   ```sh
    git clone https://github.com/kathmandu777/fastapi-django-template.git
    ```

1. Create fastapi.env with reference to fastapi.env.tmpl

1. Build

    ```sh
    docker-compose build
    ```

1. Dependency install

    ```sh
    docker-compose run --rm fastapi poetry install
    ```

1. Setup Static Files

    ```sh
    docker-compose run --rm fastapi poetry run python manage.py collectstatic --noinput
    ```

1. Migrate

    ```sh
    docker-compose run --rm fastapi poetry run python manage.py migrate
    ```

1. Create Super User for Admin Page

    ```sh
    docker-compose run --rm fastapi poetry run python manage.py createsuperuser
    ```

1. Start Server

    ```sh
    docker-compose up
    ```

## alias for frequently used commands

```sh
source alias.sh
```
