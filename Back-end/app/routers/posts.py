import os
import uuid
from fastapi import APIRouter, Depends, Form, HTTPException, File, Path, UploadFile, Query
from typing import Optional
from sqlalchemy import and_, or_, asc, desc
from database import SessionLocal
from starlette import status
from datetime import timedelta
from typing import List, Dict, Union, Any
from PIL import Image

from models import Users, Posts, Comments
from schemas import PostData
from funcs.check_token import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.get("/create", status_code=status.HTTP_200_OK)
def create_post_page(payload: Dict[str, Union[str, timedelta]] = Depends(get_current_user)):
    return {"message": "This is posting page."}

@router.post("/create", status_code=status.HTTP_200_OK)
async def create_post(
    file: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    hashtag: str = Form(...),
    payload: Dict[str, Union[str, timedelta]] = Depends(get_current_user)
    ):
    
    db = SessionLocal()
    logined_user = db.query(Users.id, Users.username, Users.gender, Users.phone_number).filter(Users.username == payload["sub"]).first()

    new_post = Posts(
        title=title,
        content=content,
        image_path=file,
        hash_tag=hashtag,
        user_id=logined_user['id']
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    post_id = db.query(Posts.id).filter(Posts.user_id == logined_user.id)[-1]
    db.close()

    return {"message": "Post Uploaded!", "post_id":post_id}

@router.get("/", status_code=status.HTTP_200_OK)
def search_post(
    user_id: Optional[int] = Query(None, description="user_id"),
    payload: Dict[str, Union[str, timedelta]] = Depends(get_current_user)
    ):
    
    db = SessionLocal()    
    if not user_id:
        posts_list = db.query(Posts).all()
    else:
        logined_user = db.query(Users.id, Users.username, Users.gender, Users.phone_number).filter(Users.username == payload["sub"]).first()
        posts_list = db.query(Posts).filter(Posts.user_id == logined_user.id).all()
    db.close()

    return posts_list

@router.post("/", status_code=status.HTTP_200_OK)
def search_hashtag(
    hashtag: str
    ):

    db = SessionLocal()
    post_lists = db.query(Posts).filter(Posts.hash_tag.like(f'%{hashtag}%')).all()
    db.close()
    return post_lists
    

@router.get("/detail/{post_id}", status_code=status.HTTP_200_OK)
def get_detailed_post(post_id: int):
    db = SessionLocal()
    one_post = db.query(Posts).filter(Posts.id == post_id).first()
    comments = db.query(Comments).filter(Comments.post_id == post_id).all()
    data = {}
    data["title"] = one_post.title
    data["content"] = one_post.content
    data["image_path"] = one_post.image_path
    data["hash_tag"] = one_post.hash_tag
    data["user_id"] = one_post.user_id
    data["comments"] = comments
    db.close()

    if not one_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    return data

@router.post("/detail/{post_id}", status_code=status.HTTP_200_OK)
def upload_comment(post_id: int, comment: str):
    db = SessionLocal()
    new_comment = Comments(
        post_id = post_id,
        comments = comment
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    db.close()

    return {"message": "Comment Uploaded!"}