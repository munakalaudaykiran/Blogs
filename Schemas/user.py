from pydantic import BaseModel,EmailStr

class CreateUser(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    user_id:int
    first_name:str
    last_name:str
    
    class config:
        from_attributes=True



class UserLogin(BaseModel):
    email:EmailStr
    password:str



class UserLogout(BaseModel):
    user_id:int
    email:EmailStr
    password:str

class config:
    orm_mode = True