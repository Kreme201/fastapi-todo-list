from pydantic import BaseModel, EmailStr

from models.user import User


class Auth(BaseModel):
    session: str
    user: User


class RequestAuthDto(BaseModel):
    email: EmailStr
    password: str
