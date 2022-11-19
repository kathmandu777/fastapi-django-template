from uuid import UUID

from pydantic import BaseModel


class ReadUserSchema(BaseModel):
    uuid: UUID
    username: str
    email: str

    class Config:
        orm_mode = True


class CreateUserSchema(BaseModel):
    username: str
    email: str
    password: str
