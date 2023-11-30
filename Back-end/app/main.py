import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from fastapi import FastAPI
from starlette import status
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user, posts

app = FastAPI()
app.include_router(user.router)
app.include_router(posts.router)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "It's main page!"}

# uvicorn main:app --reload --port 8000