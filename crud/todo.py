from datetime import datetime
from typing import List

from models.todo import Todo
from data import todos


def create(content: str) -> bool:
    try:
        todos.append(
            Todo(
                id=max([item.id for item in todos]) + 1 if len(todos) > 0 else 1,
                status=False,
                content=content,
                created=datetime.now(),
            )
        )

        return True
    except:
        return False


def update(id: int):
    try:
        for item in todos:
            if item.id == id:
                item.status = not item.status
        return True
    except:
        return False


def delete(id: int) -> bool:
    try:
        target_idx: int = [item.id for item in todos].index(id)

        if target_idx > 0:
            del todos[target_idx]

            return True
        else:
            return False
    except:
        return False
