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

    new_todo = todo.create(content)

    return {
        "success": True,
        "data": new_todo,
    }


@router.put("/{todo_id}")
async def toggle_status_todo(todo_id: int):
    new_todo: Optional[Todo] = None

    for item in todos:
        if item.id == todo_id:
            item.status = not item.status
            new_todo = item

    return {
        "success": True,
        "data": new_todo,
    }


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    target_idx: int = [item.id for item in todos].index(todo_id)

    if target_idx > 0:
        del todos[target_idx]

        return {
            "success": True,
            "data": todos,
        }
    else:
        return {
            "success": False,
        }
