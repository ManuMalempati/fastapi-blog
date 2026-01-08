from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.config import settings
from db.session import engine
from db.base_class import Base
from apis.base import apirouter
from apps.base import app_router

def configure_staticfiles(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def include_routers(app: FastAPI):
    app.include_router(apirouter)
    app.include_router(app_router)


def start_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_routers(app)
    configure_staticfiles(app)
    return app


app = start_app()
