from fastapi import APIRouter

from . import todo

router = APIRouter()

router.include_router(todo.router, prefix="/todo", tags=["Todo"])
