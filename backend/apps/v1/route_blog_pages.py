from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import session
from db.repository.blog import retrieve_active_blogs, retrieve_blog
from db.session import get_db
from typing import Optional

templates = Jinja2Templates(directory="templates")
pages_router = APIRouter()

@pages_router.get("/")
def home(request: Request, alert: Optional[str] = None, db: session = Depends(get_db)):
    blogs = retrieve_active_blogs(db=db)
    context = {"request": request, "blogs": blogs, "alert": alert}
    return templates.TemplateResponse("blogs/home.html", context=context)

@pages_router.get("/app/blog/{id}/")
def show_blog_by_id(request: Request, id: int, db: session = Depends(get_db)):
    blog = retrieve_blog(id = id, db=db)
    context = {"request": request, "blog": blog}
    return templates.TemplateResponse("blogs/detail.html", context=context)