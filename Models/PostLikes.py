from Blogs.database import Base
from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import relationship

class PostLikes(Base):
    __tablename__ = "Post_Likes"
     
    id  = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("Users.user_id",ondelete="CASCADE"),nullable=False)
    post_id = Column(Integer,ForeignKey("Posts.post_id",ondelete="CASCADE"),nullable=False)

    owner = relationship("UserDetails",back_populates="post_likes")
    post = relationship("PostDetails",back_populates="likes")