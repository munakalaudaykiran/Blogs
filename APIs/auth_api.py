from Blogs.schemas.user import UserLogin
from Blogs.models.User import UserDetails
from sqlalchemy.orm import Session
from Blogs.utils import verify_password
from fastapi import HTTPException
from Blogs.utils import create_access_token

def authentication_user(user:UserLogin,db:Session):
    db_user = db.query(UserDetails).filter(UserDetails.email == user.email).first()
    if not db_user or not verify_password(user.password,db_user.password):
        raise HTTPException(status_code=400,detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token,"type": "bearer"}
