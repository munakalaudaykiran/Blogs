from sqlalchemy import Column,Integer,ForeignKey
from Blogs.database import Base
from sqlalchemy.orm import relationship

class Commentlikes(Base):
    __tablename__ = "comment_likes"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("Users.user_id"),nullable=False)
    comment_id = Column(Integer,ForeignKey("Comments.comment_id"),nullable=False)
    
    owner = relationship("UserDetails",back_populates="comment_likes")
    comment = relationship("CommentDetails",back_populates="likes")