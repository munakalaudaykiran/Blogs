from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext 
from Blogs.schemas.user import CreateUser, UserResponse
from Blogs.database import get_db
from Blogs.APIs import user_api

router = APIRouter()


@router.post("/",response_model=UserResponse)
def create_user(user: CreateUser, db:Session = Depends(get_db)):
    return user_api.create_user(user, db)

    

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_api.get_users(db)

