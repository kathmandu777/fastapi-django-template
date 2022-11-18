#!/bin/bash
poetry run uvicorn config.asgi:fastapi_app --reload --host 0.0.0.0 --port 8000
poetry run uvicorn config.asgi:django_app --reload --host 0.0.0.0 --port 8001
