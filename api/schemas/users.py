"""
orm_mode: True
use this:
id = data.id
instead of this:
id = data["id"]
"""

from typing import List

from pydantic import BaseModel

from api.schemas import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
