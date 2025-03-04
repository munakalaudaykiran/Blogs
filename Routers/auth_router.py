from fastapi import HTTPException,Depends
from fastapi import APIRouter
from Blogs.schemas.user import UserLogin
from sqlalchemy.orm import Session
from Blogs.database import get_db 
from Blogs.APIs.auth_api import authentication_user
from Blogs.utils import verify_access_token



router = APIRouter()

@router.post("/login")
def login(user: UserLogin,db: Session= Depends(get_db)):
    return authentication_user(user,db)

@router.get("/protected")
def protected_route(user_data: dict = Depends(verify_access_token)):
    return {"message": "You are authenticated!", "user": user_data}

