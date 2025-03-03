from fastapi import FastAPI
from sqlalchemy.orm import Session
from Blogs.database import Base, engine
from Blogs.Routers.user_router import router as user_router

from Blogs import database
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router,prefix="/user",tags=["Users"])
