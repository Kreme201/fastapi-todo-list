from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel
from typing import Optional

from data import todos
from crud import todo
from models.todo import Todo


router = APIRouter()


@router.post("/")
async def create_todo(content: str = Form("")):
    if not content:
        raise HTTPException(status_code=404, detail="Content is Required")

    return {
        "success": todo.create(content),
    }


@router.put("/{todo_id}")
async def toggle_status_todo(todo_id: int):
    return {
        "success": todo.update(todo_id),
    }


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    return {
        "success": todo.delete(todo_id),
    }
