from app.api import AuthAPI
from app.schemas import Token

from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter()


@auth_router.post("/login", response_model=Token)
async def login(
    request: Request, form_data: OAuth2PasswordRequestForm = Depends()
) -> dict[str, str]:
    return AuthAPI.login(request, form_data)
