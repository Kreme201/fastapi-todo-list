from pydantic import BaseModel, EmailStr
from typing import List, Optional


from models.todo import Todo
from models.pagination import Pagination


class ResponseDto(BaseModel):
    success: bool
    message: Optional[str]


class ResponseTodoDto(ResponseDto):
    data: List[Todo]
    pagination: Pagination


class RequestAuthDto(BaseModel):
    email: EmailStr
    password: str


class UserCreateDto(BaseModel):
    name: str
    email: EmailStr
    password: str
