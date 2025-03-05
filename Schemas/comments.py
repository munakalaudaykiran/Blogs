from pydantic import BaseModel
from datetime import datetime
    
class CreateComment(BaseModel):
    content : str
    post_id : int 


class CommentResponse(BaseModel):
    comment_id : int 
    content : str
    user_id : int 
    post_id : int 
    created_at : datetime


    class Config:
        from_attributes = True
