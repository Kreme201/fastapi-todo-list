from typing import Optional

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.pagination import Pagination
from models.user import User
from crud import todo, auth

templates = Jinja2Templates("templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    page: int = 1,
    current_user: Optional[User] = Depends(auth.get_current_user),
):
    if current_user is None:
        return RedirectResponse("/member/signin/")

    rpp: int = 5

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": current_user,
            "todos": todo.get_list(
                page=page,
                rpp=rpp,
                user=current_user,
            ),
            "pagination": Pagination(
                total=todo.get_count(
                    user=current_user,
                ),
                rpp=rpp,
                current=page,
            ),
        },
    )
