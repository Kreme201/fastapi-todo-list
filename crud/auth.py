from typing import List, Optional
from uuid import uuid4

from fastapi import Cookie

from models.auth import Auth
from models.user import User
from models.dtos import RequestAuthDto

from crud import user


sessions: List[Auth] = []


def signin(data: RequestAuthDto) -> Optional[str]:
    find_user: Optional[User] = user.get_by_email(data.email)

    if find_user is None:
        return None

    if find_user.password != data.password:
        return None

    session: str = str(uuid4())
    sessions.append(Auth(session=session, user=find_user))

    return session


def get_user(session: str) -> Optional[User]:
    if len(sessions) == 0:
        return None

    idx: int = [item.session for item in sessions].index(session)

    return sessions[idx].user if idx >= 0 else None


def get_current_user(todo_session_id: str = Cookie("")) -> Optional[User]:
    return get_user(todo_session_id) if todo_session_id else None
