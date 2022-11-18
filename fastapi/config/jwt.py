from datetime import datetime, timedelta

from django.conf import settings
from jose import jwt


def jwt_decode_handler(token: str) -> dict:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])


def create_access_token_response(
    data: dict, expires_delta: timedelta | None = None
) -> dict[str, str]:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_MINUTES)
    data.update({"exp": expire})
    return {
        "access_token": jwt.encode(
            data, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        ),
        "token_type": "bearer",
    }
