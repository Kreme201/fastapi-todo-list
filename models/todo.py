from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    status: bool
    content: str
    created: datetime
