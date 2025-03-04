from Blogs.utils import hashpassword
from Blogs.models.User import UserDetails
from Blogs.schemas.user import CreateUser,UserUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_user(users: CreateUser, db: Session):
    db_user = db.query(UserDetails).filter(UserDetails.email == users.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hashpassword(users.password)
    new_user = UserDetails(
        first_name=users.first_name,
        last_name=users.last_name,
        email=users.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(UserDetails).all()

def get_user(user_id: int ,db:Session):
    db_user = db.query(UserDetails).filter(UserDetails.user_id == user_id).first()
    if not db_user :
        raise HTTPException(status_code= 401,detail="user not found")
    return db_user

def update_user(user_id: int ,db:Session,user_update : UserUpdate):
    db_user = db.query(UserDetails).filter(UserDetails.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=401,detail="user not found")
    db_user.first_name = user_update.first_name
    db_user.last_name = user_update.last_name
    db_user.email = user_update.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(user_id: int ,db: Session):
    db_user = db.query(UserDetails).filter(UserDetails.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=401,detail="user not found")
    db.delete(db_user)
    db.commit()
    return {"details": "user deleted successfully"}
