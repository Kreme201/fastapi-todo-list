from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from data import todos
from crud import todo

templates = Jinja2Templates("templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": todos[::-1],
        },
    )


@router.post("/")
async def create_todo(content: str = Form("")):
    if not content:
        return HTMLResponse(
            content="""
                <script>
                    alert("Content is Required!!");
                    history.back();
                </script>
            """,
            status_code=200,
        )

    todo.create(content)
    return RedirectResponse("/", 303)
