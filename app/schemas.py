from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# Handles the user sending data to us
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostOut(BaseModel):
    Post: Post
    id: int

    class Config:
        orm_mode = True