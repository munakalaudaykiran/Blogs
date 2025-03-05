from fastapi import FastAPI
from sqlalchemy.orm import Session
from Blogs.database import Base, engine
from Blogs.routers.user_router import router as user_router
from Blogs.routers.auth_router import router as auth_router
from Blogs.routers.post_router import router as post_router


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth_router,prefix="/auth",tags=["Authentication"])

app.include_router(user_router,prefix="/user",tags=["Users"])



app.include_router(post_router,prefix="/posts",tags=["Posts"])