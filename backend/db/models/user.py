from db.base_class import Base
from sqlalchemy import String, Integer, Boolean, Column
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default="true")

    blogs = relationship("Blog", back_populates="author")
