from django.contrib.auth.hashers import make_password
from passlib.handlers.django import django_pbkdf2_sha256


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return django_pbkdf2_sha256.verify(plain_password, hashed_password)


def hash_password(plain_password: str) -> str:
    return make_password(plain_password)
