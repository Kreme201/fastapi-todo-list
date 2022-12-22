from pydantic import BaseModel
from typing import List, Optional


from models.todo import Todo
from models.pagination import Pagination


class ResponseDto(BaseModel):
    success: bool
    message: Optional[str]


class ResponseTodoDto(ResponseDto):
    data: List[Todo]
    pagination: Pagination
