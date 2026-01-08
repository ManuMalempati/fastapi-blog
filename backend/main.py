from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.config import settings
from db.session import engine
from db.base_class import Base
from apis.base import apirouter
from apps.base import app_router

from alembic import command
from alembic.config import Config
import os

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def configure_staticfiles(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def include_routers(app: FastAPI):
    app.include_router(apirouter)
    app.include_router(app_router)


def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # uncomment this if hosting on render
    run_migrations()
    include_routers(app)
    configure_staticfiles(app)
    return app



app = start_app()
