from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import session
from db.repository.blog import retrieve_active_blogs, retrieve_blog
from db.session import get_db
from apis.v1.route_login import get_current_user, get_optional_user
from db.models.user import User
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")
pages_router = APIRouter()

@pages_router.get("/")
def home(
    request: Request,
    alert: Optional[str] = None,
    db: session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    blogs = retrieve_active_blogs(db=db)
    context = {
        "request": request,
        "blogs": blogs,
        "alert": alert,
        "current_user": current_user
    }
    return templates.TemplateResponse("blogs/home.html", context=context)


@pages_router.get("/app/blog/{id}/")
def show_blog_by_id(
    request: Request,
    id: int,
    db: session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    blog = retrieve_blog(id=id, db=db)
    context = {
        "request": request,
        "blog": blog,
        "current_user": current_user
    }
    return templates.TemplateResponse("blogs/detail.html", context=context)

@pages_router.get("/create")
def create_blog_page(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse("blogs/create_blog.html", {"request": request})

@pages_router.get("/blog/{id}/edit")
def edit_blog_page(
    request: Request,
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    blog = retrieve_blog(id=id, db=db)

    if not blog:
        return RedirectResponse("/?alert=Blog%20Not%20Found", status_code=302)

    if blog.author_id != current_user.id:
        return RedirectResponse("/?alert=Not%20Authorized", status_code=302)

    return templates.TemplateResponse(
        "blogs/edit_blog.html",
        {"request": request, "blog": blog}
    )
