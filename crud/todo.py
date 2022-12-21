from datetime import datetime
from typing import List

from models.todo import Todo
from data import todos


def get_list(page: int = 1, rpp: int = 5) -> List[Todo]:
    return todos[::-1][(page - 1) * rpp : page * rpp]


def get_count() -> int:
    return len(todos)


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

        if target_idx >= 0:
            del todos[target_idx]

            return True
        else:
            return False
    except:
        return False
