from app.models import User
from config.exceptions import InvalidTokenException
from config.jwt import jwt_decode_handler
from jose import JWTError

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt_decode_handler(token)
    except JWTError:
        raise InvalidTokenException()

    user = User.objects.filter(uuid=payload.get("sub", "")).first()
    if not user:
        raise InvalidTokenException()
    return user


async def get_current_admin_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user
