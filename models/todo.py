from datetime import datetime
from pydantic import BaseModel

from models.user import User


class Todo(BaseModel):
    id: int
    status: bool
    content: str
    author: User
    created: datetime
