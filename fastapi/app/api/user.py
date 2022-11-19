from logging import getLogger

from app.models import User
from app.schemas import CreateUserSchema
from asgiref.sync import sync_to_async
from config.password import hash_password

from fastapi import HTTPException, Request

logger = getLogger(__name__)


class UserAPI:
    @classmethod
    def get(cls, request: Request, current_user: User) -> User:
        return current_user

    @classmethod
    async def create(cls, request: Request, schema: CreateUserSchema) -> User:
        user = await User.objects.filter(email=schema.email).afirst()
        if user:
            raise HTTPException(status_code=400, detail="Email already registered")
        schema.password = hash_password(schema.password)
        return await sync_to_async(User.objects.create)(**schema.dict())
