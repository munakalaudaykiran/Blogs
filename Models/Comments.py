from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from Blogs.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class CommentDetails(Base):
    __tablename__ = "Comments"
    comment_id  = Column(Integer,primary_key=True,index=True)
    content =  Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("Users.user_id",ondelete="CASCADE"),nullable=False)
    post_id = Column(Integer,ForeignKey("Posts.post_id",ondelete="CASCADE"),nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)

    owner = relationship("UserDetails",back_populates="comments")
    post = relationship("PostDetails",back_populates="comments")