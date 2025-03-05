from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import datetime
from jose import jwt,JWTError
from fastapi import HTTPException,Depends
from Blogs.database import get_db
from sqlalchemy.orm import Session
from Blogs.models.User import UserDetails
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOEKN_EXPIRE_MINUTES  = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashpassword(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow()+datetime.timedelta(minutes=ACCESS_TOEKN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  
        email = payload.get("sub")  

        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = db.query(UserDetails).filter(UserDetails.email == email).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return {"user_id": user.user_id,"first_name":user.first_name,"last_name":user.last_name}  

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")



