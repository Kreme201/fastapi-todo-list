from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel
from typing import Optional

from data import todos
from crud import todo
from models.todo import Todo


class ResponseDto(BaseModel):
    success: bool


router = APIRouter()


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
