from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.views import router as view_router
from routers.api.v1 import router as api_v1_router


app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(view_router, include_in_schema=False)
app.include_router(api_v1_router, prefix="/api/v1")


if __name__ == "__main__":
    from uvicorn import run

    run("main:app", reload=True)
