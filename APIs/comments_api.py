from Blogs.schemas.comments import CreateComment
from sqlalchemy.orm import Session
from Blogs.models.Comments import CommentDetails
from fastapi import HTTPException
def create_comment(comment : CreateComment,db : Session,user_id : int ):
    new_comment = CommentDetails(content = comment.content,post_id = comment.post_id,user_id = user_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comments_by_post(post_id : int, db: Session):
    return db.query(CommentDetails).filter(CommentDetails.post_id == post_id).all()

def delete_comment(comment_id : int, db:Session,current_user):
    comment = db.query(CommentDetails).filter(CommentDetails.comment_id == comment_id).first()
    if not comment: 
        raise HTTPException(status_code=404,detail="comment not found")

    if comment.user_id !=current_user["user_id"]:
        raise HTTPException (status_code=403 , detail="not authorized to delete the commen")

    db.delete(comment)
    db.commit()

    return {"message": "comment deleted successfully"}   

