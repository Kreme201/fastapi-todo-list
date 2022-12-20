from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: int
    status: bool
    content: str
    created: datetime
