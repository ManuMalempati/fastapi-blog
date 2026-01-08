from fastapi import APIRouter
from apps.v1 import route_blog_pages, route_login

app_router = APIRouter()

app_router.include_router(route_blog_pages.pages_router, prefix="", tags=["home"])

app_router.include_router(router=route_login.router, prefix="/auth", tags=[""], include_in_schema=False)

