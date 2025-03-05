from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreatePost(BaseModel):
    title: str
    content : str

class PostResponse(BaseModel):
    post_id: int 
    title : str
    content : str
    user_id: int 
    created_at : datetime
    updated_at : datetime
    
    class Config:
        from_attributes =True

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

    class Config:
        from_attributes = True