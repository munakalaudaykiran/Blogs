from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from Blogs.utils import verify_access_token
from Blogs.database import get_db
from Blogs.APIs.postlikes_api import like_post as like_post_api,dislike_post as dislike_post_api,count_likes 
router = APIRouter()

@router.post("/{post_id}/like")
def like_post(post_id : int,db : Session = Depends(get_db),current_user : dict = Depends(verify_access_token)):
    return like_post_api(post_id,db,current_user)

@router.post("/{post_id}/dislike")
def dislike_post(post_id : int ,db : Session = Depends(get_db),current_user : dict = Depends(verify_access_token)):
    return dislike_post_api(post_id,db,current_user)

@router.get("/postlikes/{post_id}/count")
def get_like_count(post_id : int ,db :Session = Depends(get_db)):
    return count_likes(post_id, db)