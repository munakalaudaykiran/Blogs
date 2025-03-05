from sqlalchemy import Column, String, Integer
from sqlalchemy.sql import func
from Blogs.database import Base
from sqlalchemy.orm import relationship

class UserDetails(Base):
    __tablename__ = "Users"
    user_id = Column(Integer,primary_key=True,nullable=False,index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    email = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)

    posts = relationship("PostDetails", back_populates="owner", cascade="all, delete")
    comments = relationship("CommentDetails", back_populates="owner", cascade="all, delete")
