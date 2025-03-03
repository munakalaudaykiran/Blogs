from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext 
from Blogs.Schemas import user
from Blogs.database import get_db
from Blogs.APIs import user_api

router=APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/",response_model=user.UserResponse)
def create_user(user: user.CreateUser,db:Session = Depends(get_db)):
    return user_api.user_api(user,db)


