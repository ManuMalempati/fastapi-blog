from fastapi import APIRouter, Depends, status, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from db.repository.blog import create_new_blog, retrieve_blog, retrieve_active_blogs, update_blog_by_id, delete_blog_by_id
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from typing import List, Optional
from db.models.user import User
from apis.v1.route_login import get_current_user

router = APIRouter()

# submission via postman
@router.post(path="/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return blog

# for page submission instead of postman
@router.post("/create-form")
def create_blog_form(
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    blog_data = CreateBlog(title=title, slug=slug, content=content)
    create_new_blog(blog=blog_data, db=db, author_id=current_user.id)
    return RedirectResponse("/?alert=Blog%20Created", status_code=302)

@router.get(path="/active_blogs", response_model=List[ShowBlog])
def get_blog(db: Session = Depends(get_db)):
    blogs = retrieve_active_blogs(db)
    return blogs


@router.get(path="/{id}", response_model=ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id, db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} does not exist.")
    else:
        return blog
    
@router.put(path="/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = update_blog_by_id(id=id, blog=blog, db=db, author_id=current_user.id)
    if isinstance(blog, dict):
        raise HTTPException(
            detail=blog.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    else:
        return blog
    
    
@router.delete(path="/{id}")
def delete_a_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    message = delete_blog_by_id(id=id, db=db, author_id=current_user.id)
    if message.get("error"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message.get("error"))
    return {"msg": message.get("msg")}

@router.post("/{id}/delete")
def delete_blog_page(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    blog = retrieve_blog(id=id, db=db)

    if not blog:
        return RedirectResponse("/?alert=Blog%20Not%20Found", status_code=302)

    if blog.author_id != current_user.id:
        return RedirectResponse("/?alert=Not%20Authorized", status_code=302)

    delete_blog_by_id(id=id, db=db, author_id=current_user.id)
    return RedirectResponse("/?alert=Blog%20Deleted", status_code=302)

@router.post("/{id}/edit")
def edit_blog_submit(
    id: int,
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    blog = retrieve_blog(id=id, db=db)

    if not blog:
        return RedirectResponse("/?alert=Blog%20Not%20Found", status_code=302)

    if blog.author_id != current_user.id:
        return RedirectResponse("/?alert=Not%20Authorized", status_code=302)

    update_data = UpdateBlog(title=title, slug=slug, content=content)
    update_blog_by_id(id=id, blog=update_data, db=db, author_id=current_user.id)

    return RedirectResponse("/?alert=Blog%20Updated", status_code=302)
