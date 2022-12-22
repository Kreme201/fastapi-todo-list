from fastapi import APIRouter

from . import todo, user

router = APIRouter()

router.include_router(todo.router, prefix="/todo", tags=["Todo"])
router.include_router(user.router, prefix="/user", tags=["User"])
