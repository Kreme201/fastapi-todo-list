from fastapi import APIRouter

from . import main, member

router = APIRouter()

router.include_router(main.router)
router.include_router(member.router, prefix="/member")
