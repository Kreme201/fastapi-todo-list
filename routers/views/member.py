from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from crud import auth
from models.user import User

router = APIRouter()
templates = Jinja2Templates("templates")


@router.get("/signin", response_class=HTMLResponse)
async def signin(request: Request, current_user: User = Depends(auth.get_current_user)):
    if current_user is not None:
        return RedirectResponse("/")

    return templates.TemplateResponse(
        "member/signin.html",
        {
            "request": request,
            "user": None,
        },
    )


@router.get("/signup", response_class=HTMLResponse)
async def signup(request: Request, current_user: User = Depends(auth.get_current_user)):
    if current_user is not None:
        return RedirectResponse("/")

    return templates.TemplateResponse(
        "member/signup.html",
        {
            "request": request,
            "user": None,
        },
    )
