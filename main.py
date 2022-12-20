from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import views
from routers.api.v1 import api


app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(views.router, include_in_schema=False)
app.include_router(api.router, prefix="/api/v1")

if __name__ == "__main__":
    from uvicorn import run

    run("main:app", reload=True)
