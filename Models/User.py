from sqlalchemy import Column,String,Integer
from sqlalchemy.sql import func
from Blogs.database import Base

def UserDetails(Base):
    __tablename__ = "Users"
    user_id = Column(Integer,primary_key=True,nullable=False,index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    email = Column(String,unique=True,nullable=False,primary_key=True)
    password = Column(String,nullable=False)
