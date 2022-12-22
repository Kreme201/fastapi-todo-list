from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.pagination import Pagination
from crud import todo

templates = Jinja2Templates("templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, page: int = 1):
    rpp: int = 5

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": todo.get_list(
                page=page,
                rpp=rpp,
            ),
            "pagination": Pagination(
                total=todo.get_count(),
                rpp=rpp,
                current=page,
            ),
        },
    )
