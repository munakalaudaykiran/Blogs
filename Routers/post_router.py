from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Blogs.database import get_db
from Blogs.schemas.post import CreatePost, PostResponse,PostUpdate
from Blogs.APIs import post_api
from Blogs.utils import verify_access_token

router = APIRouter()

@router.post("/", response_model=PostResponse)
def create_post(post: CreatePost,db: Session = Depends(get_db),user_data: dict = Depends(verify_access_token)):
    user_id = user_data["user_id"]
    return post_api.create_post(post, db, user_id)


@router.get("/", response_model=list[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return post_api.get_posts(db)

@router.get("/{post_id}",response_model=PostResponse)
def get_post(post_id : int ,db :Session =Depends(get_db),user_data : dict = Depends(verify_access_token)):
    return post_api.get_post(post_id,db)

@router.put("/{post_id}",response_model=PostResponse)
def update_post(post_id: int,post_update: PostUpdate, db: Session = Depends(get_db), user: dict = Depends(verify_access_token)):
    return post_api.update_post(post_id, post_update, db, user)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), user: dict = Depends(verify_access_token)):
    return post_api.delete_post(post_id, db, user)