from sqlalchemy.orm import Session
from fastapi import HTTPException
from Blogs.models.PostLikes import PostLikes
from sqlalchemy.sql import func
def like_post(post_id : int ,db : Session, current_user):
    existing_like = db.query(PostLikes).filter(PostLikes.post_id == post_id, PostLikes.user_id == current_user["user_id"]).first()

    if existing_like:
        raise HTTPException(status_code=400, detail="Post already liked")

    like = PostLikes(user_id=current_user["user_id"], post_id=post_id)
    db.add(like)
    db.commit()
    return {"message": "Post liked successfully"}


def dislike_post(post_id : int ,db : Session, current_user):
    like = db.query(PostLikes).filter(PostLikes.post_id == post_id, PostLikes.user_id == current_user["user_id"]).first()

    if not like:
        raise HTTPException(status_code=404, detail="Like not found")

    db.delete(like)
    db.commit()
    return {"message": "Like removed successfully"}

def count_likes(post_id : int ,db :Session):
    like_count = db.query(func.count(PostLikes.id)).filter(PostLikes.post_id == post_id).scalar()
    return {"post_id": post_id, "likes": like_count}