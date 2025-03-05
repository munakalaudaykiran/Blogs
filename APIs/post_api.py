from Blogs.schemas.post import CreatePost
from sqlalchemy.orm import Session
from Blogs.models.Post import PostDetails
from fastapi import HTTPException
from Blogs.schemas.post import PostUpdate,PostResponse



def create_post(post:CreatePost,db:Session,user_id: int):
    new_post = PostDetails(title = post.title,content = post.content,user_id = user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db:Session):
    return db.query(PostDetails).all()

def get_post(post_id : int ,db : Session):
    db_post = db.query(PostDetails).filter(PostDetails.post_id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404,detail="post not found")
    return PostResponse.model_validate(db_post) 

def update_post(post_id: int, post_update: PostUpdate, db: Session, user: dict):
    db_post = db.query(PostDetails).filter(PostDetails.post_id==post_id ).first()
    if not db_post:
        raise HTTPException(status_code=404,detail="post not found")
    if db_post.user_id != user["user_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")

    for key, value in post_update.dict(exclude_unset=True).items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(post_id : int, db:Session ,user : dict):
    db_post = db.query(PostDetails).filter(PostDetails.post_id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404,detail="post not found")
    
    if db_post.user_id != user["user_id"]:
        raise HTTPException(status_code=403,detail="not authorized to delete the post")
    
    db.delete(db_post)
    db.commit()
    return {"message" :"post deleted successfully"}