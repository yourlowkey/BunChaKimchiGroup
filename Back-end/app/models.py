import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from sqlalchemy import TEXT, Column, INTEGER, String, Boolean, TIMESTAMP, LargeBinary, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)

class Posts(Base):
    __tablename__ = "posts"

    id = Column(INTEGER, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(TEXT, nullable=False)
    image_path = Column(TEXT, nullable=False)
    hash_tag = Column(String, nullable=False)
    user_id = Column(INTEGER, ForeignKey("users.id"), nullable=False)


class Comments(Base):
    __tablename__ = "comments"

    id = Column(INTEGER, primary_key=True)
    post_id = Column(INTEGER, ForeignKey("posts.id"), nullable=False)
    comments = Column(String, nullable=False)