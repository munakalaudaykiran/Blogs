from fastapi import APIRouter,Depends
from Blogs.schemas.comments import CommentResponse,CreateComment
from sqlalchemy.orm import Session
from Blogs.database import get_db
from Blogs.utils import verify_access_token
from Blogs.APIs import comments_api
router =  APIRouter()

@router.post("/",response_model=CommentResponse)
def create_comment(comment : CreateComment , db : Session = Depends(get_db),user : dict =Depends(verify_access_token)):
    return comments_api.create_comment(comment,db,user["user_id"])


@router.get("/{post_id}",response_model=list[CommentResponse])
def get_comments(post_id : int ,db : Session = Depends(get_db)):
    return comments_api.get_comments_by_post(post_id,db)

@router.delete("/{comment_id}")
def delete_comment(comment_id : int ,db:Session = Depends(get_db),current_user = Depends(verify_access_token)):
    return comments_api.delete_comment(comment_id,db,current_user)
