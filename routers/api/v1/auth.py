from typing import Optional

from fastapi import APIRouter, Response

from models.response import ResponseDto
from models.auth import Auth, RequestAuthDto
from crud import auth

router = APIRouter()


@router.post("/")
def signin(response: Response, data: RequestAuthDto) -> ResponseDto:
    session: Optional[str] = auth.signin(data)

    if session:
        response.set_cookie(key="todo_session_id", value=session, httponly=True)
        return ResponseDto(success=True)

    return ResponseDto(
        success=False,
        message="이메일과 비밀번호를 확인해주세요!!",
    )
