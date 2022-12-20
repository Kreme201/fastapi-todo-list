from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import views

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(views.router)
