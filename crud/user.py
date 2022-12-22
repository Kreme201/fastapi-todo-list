from typing import List, Optional

from models.user import User, UserCreateDto

users: List[User] = []


def create(data: UserCreateDto) -> bool:
    try:
        users.append(
            User(
                id=max([item.id for item in users]) + 1 if len(users) > 0 else 1,
                name=data.name,
                email=data.email,
                password=data.password,
            )
        )

        return True
    except:
        return False


def get_by_id(user_id: int) -> Optional[User]:
    try:
        idx: int = [item.id for item in users].index(user_id)

        return users[idx] if idx >= 0 else None
    except:
        return None


def get_by_email(email: str) -> Optional[User]:
    try:
        idx: int = [item.email for item in users].index(email)

        return users[idx] if idx >= 0 else None
    except:
        return None
