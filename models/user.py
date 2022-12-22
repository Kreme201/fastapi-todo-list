from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class UserCreateDto(BaseModel):
    name: str
    email: EmailStr
    password: str
