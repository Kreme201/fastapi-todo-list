from fastapi import APIRouter, HTTPException, Form, Depends

from crud import todo, auth
from models.response import ResponseDto, ResponseTodoDto
from models.pagination import Pagination
from models.user import User

router = APIRouter()


@router.get("/")
async def get_todos(
    page: int = 1,
    rpp: int = 5,
    user: User = Depends(auth.get_current_user),
) -> ResponseTodoDto:
    try:
        return ResponseTodoDto(
            success=True,
            data=todo.get_list(
                page=page,
                rpp=rpp,
                user=user,
            ),
            pagination=Pagination(
                total=todo.get_count(
                    user=user,
                ),
                rpp=rpp,
                current=page,
            ),
        )
    except:
        return ResponseTodoDto(
            success=False,
            data=[],
            pagination=Pagination(),
        )


@router.post("/")
async def create_todo(
    content: str = Form(""), user: User = Depends(auth.get_current_user)
) -> ResponseDto:
    if not content:
        raise HTTPException(status_code=404, detail="Content is Required")

    return ResponseDto(
        success=todo.create(
            content=content,
            user=user,
        ),
    )


@router.put("/{todo_id}")
async def toggle_status_todo(
    todo_id: int, user: User = Depends(auth.get_current_user)
) -> ResponseDto:
    return ResponseDto(
        success=todo.update(
            id=todo_id,
            user=user,
        ),
    )


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int, user: User = Depends(auth.get_current_user)
) -> ResponseDto:
    return ResponseDto(
        success=todo.delete(
            id=todo_id,
            user=user,
        ),
    )
