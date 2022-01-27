from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# Handles the user sending data to us
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


# Handles us sending back data to the users
class Post(PostBase):
    id: int
    created_at: datetime

    # class Config:
    #     # tells the Pydantic model to read the data even if it is not a dict, but an ORM model
    #     orm_mode = True
