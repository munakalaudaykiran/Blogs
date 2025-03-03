from Blogs.utils import hashpassword
from Blogs.Models import User
from Blogs.Schemas import user
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_user(users: user.CreateUser,db: Session):
    db_user = db.query(User.UserDetails).filter(User.email == users.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hashpassword(users.password)
    new_user = User.UserDetails(first_name=users.first_name,last_name=users.last_name,email=users.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# def get_users(db:Session):
#     return db.query(User.UserDetails).all()
