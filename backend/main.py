from fastapi import FastAPI, Depends, HTTPException
from core.config import settings
from typing import Dict
from db.session import engine
from apis.base import apirouter
from apps.base import app_router
from fastapi.staticfiles import StaticFiles

def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def include_router(app):
    app.include_router(apirouter)
    app.include_router(app_router)

# Propogate changes to database via alembic instead of createall to make sure we have versioning
def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_staticfiles(app)
    return app

app = start_app()