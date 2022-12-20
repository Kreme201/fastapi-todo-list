from datetime import datetime
from typing import List

from models.todo import Todo
from data import todos


def create(content: str) -> Todo:
    new_todo = Todo(
        id=max([item.id for item in todos]) + 1 if len(todos) > 0 else 1,
        status=False,
        content=content,
        created=datetime.now(),
    )

    todos.append(new_todo)

    return new_todo


def update(id: int, status: bool) -> List[Todo]:
    for item in todos:
        if item.id == id:
            item.status = status
    return todos


def delete(id: int) -> List[Todo]:
    todos = [item for item in todos if item.id != id]
    return todos
