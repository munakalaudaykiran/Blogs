from pydantic import BaseModel,EmailStr

class CreateUser(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    password:str

class UserResponse(CreateUser):
    user_id:int
    first_name:str
    last_name:str
    
    class config:
        orm_mode=True




class UserLogin(BaseModel):
    email:EmailStr
    password:str



class UserLogout(BaseModel):
    user_id:int
    email:EmailStr
    password:str

class config:
    orm_mode = True