from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from Blogs.database import Base
from Blogs.models.User import UserDetails
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class PostDetails(Base):
    __tablename__ = "Posts"
    post_id = Column(Integer,index=True,primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    user_id = Column(Integer, ForeignKey("Users.user_id"),nullable=False)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,default=func.now(),onupdate= func.now())

    owner = relationship("UserDetails", back_populates="posts")