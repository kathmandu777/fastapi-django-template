#!/bin/bash
poetry run gunicorn -c gunicorn.conf.fastapi.py
poetry run gunicorn -c gunicorn.conf.django.py
