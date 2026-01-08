from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog
from core.hashing import Hasher

def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    db_blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id,
        is_active=True
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id==id).first()
    return blog

def retrieve_active_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    return blogs

def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int = 1):
    blog_in_db = db.query(Blog).filter(Blog.id==id).first()
    if not blog_in_db:
        return {"error": f"blog with id {id} does not exist"}
    if blog_in_db.author_id != author_id:
        return {"error": f"only the author can modify the blog"}
    blog_in_db.title = blog.title
    blog_in_db.slug = blog.slug
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db

def delete_blog_by_id(id: int, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id==id)
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id: {id}"}
    if blog_in_db.first().author_id != author_id:
        return {"error": "only the author can delete the blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"Successfully deleted blog with id: {id}"}

