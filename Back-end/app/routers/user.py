import os
from fastapi import APIRouter, HTTPException, Depends, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from database import SessionLocal
from datetime import timedelta
from typing import Dict
from dotenv import load_dotenv
load_dotenv()  # .env 파일을 활성화

from schemas import UserData
from models import Users
from funcs.hash_password import HashPassword
from jwt_utils import create_access_token

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

SECRET_KEY = os.getenv("SECRET_KEY")
manager = LoginManager(SECRET_KEY, '/login', use_cookie=True)
ACCESS_TOKEN_EXPIRE_MINUTES = 6000
hash_password = HashPassword()

@router.get("/login", status_code=status.HTTP_200_OK)
def login() -> Dict[str, str]:
    return {"message": "This is login page."}

@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    response: Response,
    user_input: OAuth2PasswordRequestForm = Depends()
    ) -> Dict[str, str]:

    # check username in db
    db = SessionLocal()
    user_exist = db.query(Users).filter(Users.username == user_input.username).first()

    if not user_exist:
        db.close()
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Please check your username and password and try again."
        )

    # if username in db -> check password -> return access_token
    if hash_password.verify_hash(user_input.password, user_exist.password):
        user_data = db.query(Users).filter(Users.username == user_input.username).first()
        db.close()
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user_input.username}, expires_delta=access_token_expires
        )
        # cookie: access_token
        response.set_cookie(key="access_token", value=access_token)

        # user_info = {}
        # user_info[""]
        return {
            "user_info": user_data,
            "access_token": access_token,
            "token_type": "Bearer"
        }
    db.close()
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )


@router.get("/register", status_code=status.HTTP_200_OK)
def register() -> Dict[str, str]:
    return {"message": "This is register page."}

@router.post("/register", status_code=status.HTTP_200_OK)
def register(data: UserData) -> Dict[str, str]:
    # check user in db
    # if user is already in db, raise http exception
    # if user is not in db, add data to db
    db = SessionLocal()
    temp_user = db.query(Users).filter(Users.username == data.username).first()
    if temp_user:
        db.close()
        raise HTTPException(status_code=400, detail="This user already registered.")
    else:
        hashed_password = hash_password.create_hash(data.password)
        new_user = Users(
            username=data.username,
            password=hashed_password,
            gender=data.gender,
            phone_number=data.phone_number
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()
    
    data = {
        "username":data.username, 
        "password": data.password, 
        "gender": data.gender, 
        "phone_number": data.phone_number
        }
    return data