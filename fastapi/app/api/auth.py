from app.models import User
from config.exceptions import (
    InvalidCredentialsException,
    InvalidEmailOrPasswordException,
)
from config.jwt import create_access_token_response
from config.password import verify_password

from fastapi import Request
from fastapi.security import OAuth2PasswordRequestForm


class AuthAPI:
    @classmethod
    def login(
        cls, request: Request, form_data: OAuth2PasswordRequestForm
    ) -> dict[str, str]:
        credentials = {"email": form_data.username, "password": form_data.password}

        if all(credentials.values()):
            user = cls()._authenticate_user(**credentials)
        else:
            raise InvalidCredentialsException()
        return create_access_token_response({"sub": str(user.uuid)})

    def _authenticate_user(self, email: str, password: str) -> User:
        user = User.objects.filter(email=email).first()

        if not user:
            raise InvalidEmailOrPasswordException()
        if not verify_password(password, user.password) or not user.is_active:
            raise InvalidEmailOrPasswordException()
        return user
