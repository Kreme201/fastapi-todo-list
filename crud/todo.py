from datetime import datetime
from typing import List

from models.todo import Todo
from models.user import User

todos: List[Todo] = []


def get_list(user: User, page: int = 1, rpp: int = 5) -> List[Todo]:
    own_items = [item for item in todos if item.author.id == user.id][::-1]
    return own_items[(page - 1) * rpp : page * rpp]


def get_count(user: User) -> int:
    return len([item for item in todos if item.author.id == user.id])


def create(content: str, user: User) -> bool:
    try:
        todos.append(
            Todo(
                id=max([item.id for item in todos]) + 1 if len(todos) > 0 else 1,
                status=False,
                content=content,
                author=user,
                created=datetime.now(),
            )
        )

        return True
    except:
        return False


def update(id: int, user: User):
    try:
        for item in todos:
            if item.id == id and item.author.id == user.id:
                item.status = not item.status
        return True
    except:
        return False


def delete(id: int, user: User) -> bool:
    try:
        target_idx: int = [item.id for item in todos].index(id)

        if target_idx >= 0 and todos[target_idx].author.id == user.id:
            del todos[target_idx]

            return True
        else:
            return False
    except:
        return False
