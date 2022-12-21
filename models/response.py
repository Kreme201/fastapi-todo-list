from pydantic import BaseModel
from typing import List


from models.todo import Todo
from models.pagination import Pagination


class ResponseDto(BaseModel):
    success: bool


class ResponseTodoDto(ResponseDto):
    data: List[Todo]
    pagination: Pagination
