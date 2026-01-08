from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher
from sqlalchemy.exc import IntegrityError

def create_new_user(user: UserCreate, db: Session):
    normalized_email = user.email.strip().lower()

    db_user = User(
        email=normalized_email,
        password=Hasher.hash_password(user.password),
        is_active=True
    )

    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(db_user)
    return db_user

