from typing import Optional

from fastapi import APIRouter, Form, Depends

from models.user import User, UserCreateDto
from models.response import ResponseDto
from crud import user

router = APIRouter()


@router.post("/")
def create_user(data: UserCreateDto) -> ResponseDto:
    if user.get_by_email(data.email) is not None:
        return ResponseDto(
            success=False,
            message="이미 가입된 이메일입니다!!",
        )
    return ResponseDto(
        success=user.create(data),
    )
