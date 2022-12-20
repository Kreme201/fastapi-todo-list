from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from data import todos
from models.todo import Todo
from models.pagination import Pagination

templates = Jinja2Templates("templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, page: int = 1):
    rpp: int = 5
    data: List[Todo] = todos[::-1][(page - 1) * rpp : page * rpp]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": data,
            "total": len(todos),
            "page": page,
            "rpp": rpp,
            "pagination": Pagination(total=len(todos), rpp=rpp, current=page),
        },
    )
