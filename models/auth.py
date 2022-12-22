from pydantic import BaseModel

from models.user import User


class Auth(BaseModel):
    session: str
    user: User
