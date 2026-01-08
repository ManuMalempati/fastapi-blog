from fastapi import APIRouter
from apis.v1 import route_user, route_login, route_blog

apirouter = APIRouter()

apirouter.include_router(router=route_user.router, prefix="/user", tags=["users"])

apirouter.include_router(router=route_blog.router, prefix="/blog", tags=["blogs"])

apirouter.include_router(router=route_login.router, prefix="/login", tags=["login"])