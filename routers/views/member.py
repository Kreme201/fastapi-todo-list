from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates("templates")


@router.get("/signin", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse("member/signin.html", {"request": request})


@router.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("member/signup.html", {"request": request})
