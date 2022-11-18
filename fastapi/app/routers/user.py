from app.api import UserAPI
from app.dependencies.auth import get_current_user
from app.models import User
from app.schemas import CreateUserSchema, ReadUserSchema

from fastapi import APIRouter, Depends, Request

user_router = APIRouter()


@user_router.get("/", response_model=ReadUserSchema)
async def get(request: Request, current_user: User = Depends(get_current_user)) -> User:
    return UserAPI.get(request, current_user)


@user_router.post(
    "/",
    response_model=ReadUserSchema,
)
async def create(request: Request, schema: CreateUserSchema) -> User:
    return UserAPI.create(request, schema)
