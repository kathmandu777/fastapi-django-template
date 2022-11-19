# Fastapi x Django Template

## Overview

DB周り(admin, ORM)はDjangoの機能を用いて、API周りはFastAPIを用いてサーバーを実装する際のテンプレートリポジトリです。

## Prerequisites

### Poetry

Pythonファイルの依存関係管理はpoetryを使用します。

1. <https://python-poetry.org/docs/#installation>
1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install --upgrade pip` (必要であれば)
1. `poetry install`

### pre-commit (for developers)

commitする前に実行するコマンドを定義するツールです。`.pre-commit-config.yaml` に定義済みなので、それを各自の環境に設定する必要があります。下記手順で行ってください。

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
