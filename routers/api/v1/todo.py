from fastapi import APIRouter, HTTPException, Form

from crud import todo
from models.response import ResponseDto, ResponseTodoDto
from models.pagination import Pagination

router = APIRouter()


@router.get("/")
async def get_todos(page: int = 1, rpp: int = 5) -> ResponseTodoDto:
    try:
        return ResponseTodoDto(
            success=True,
            data=todo.get_list(page, rpp),
            pagination=Pagination(
                total=todo.get_count(),
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
async def create_todo(content: str = Form("")) -> ResponseDto:
    if not content:
        raise HTTPException(status_code=404, detail="Content is Required")

    return ResponseDto(success=todo.create(content))


@router.put("/{todo_id}")
async def toggle_status_todo(todo_id: int) -> ResponseDto:
    return ResponseDto(success=todo.update(todo_id))


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int) -> ResponseDto:
    return ResponseDto(success=todo.delete(todo_id))
