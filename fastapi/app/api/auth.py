from logging import getLogger

from app.models import User
from config.exceptions import (
    InvalidCredentialsException,
    InvalidEmailOrPasswordException,
)
from config.jwt import create_access_token_response
from config.password import verify_password

from fastapi import Request
from fastapi.security import OAuth2PasswordRequestForm

logger = getLogger(__name__)


class AuthAPI:
    @classmethod
    async def login(
        cls, request: Request, form_data: OAuth2PasswordRequestForm
    ) -> dict[str, str]:
        credentials = {"email": form_data.username, "password": form_data.password}

        if all(credentials.values()):
            user = await cls()._authenticate_user(**credentials)
        else:
            raise InvalidCredentialsException()
        return create_access_token_response({"sub": str(user.uuid)})

    async def _authenticate_user(self, email: str, password: str) -> User:
        user = await User.objects.filter(email=email).afirst()
        if not user:
            raise InvalidEmailOrPasswordException()
        if not verify_password(password, user.password) or not user.is_active:
            raise InvalidEmailOrPasswordException()
        return user
