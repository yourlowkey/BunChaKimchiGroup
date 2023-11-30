from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional

class UserData(BaseModel):
    username: str
    password: str
    gender: str
    phone_number: str

class PostData(BaseModel):
    title: str
    content: str
    image_path: str
    hashtag: str
    user_id: int