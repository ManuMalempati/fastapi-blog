from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher
from fastapi import HTTPException, status

def create_new_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    
    db_user = User(
        email=user.email,
        password=Hasher.hash_password(user.password),
        is_active=True
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
