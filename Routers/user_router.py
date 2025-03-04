from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext 
from Blogs.schemas.user import CreateUser, UserResponse,UserUpdate
from Blogs.database import get_db
from Blogs.APIs import user_api

router = APIRouter()


@router.post("/",response_model=UserResponse)
def create_user(user: CreateUser, db:Session = Depends(get_db)):
    return user_api.create_user(user, db)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_api.get_users(db)

@router.get("/{user_id}",response_model=UserResponse)
def get_user(user_id: int ,db:Session = Depends(get_db)):
    return user_api.get_user(user_id,db)

@router.put("/{user_id}",response_model=UserResponse)
def update_user(user_id: int,user_update: UserUpdate,db:Session = Depends(get_db)):
    return user_api.update_user(user_id,db,user_update)

@router.delete("/{user_id}")
def delete_user(user_id : int ,db: Session = Depends(get_db)):
    return user_api.delete_user(user_id,db)