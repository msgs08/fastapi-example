"""
orm_mode: True
use this:
id = data.id
instead of this:
id = data["id"]
"""

from typing import Union

from pydantic import BaseModel


# ItemBase -> BaseItem, like BaseModel
class BaseItem(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemToCreate(BaseItem):
    pass


class ItemToUpdate(BaseItem):
    pass


class Item(BaseItem):
    id: int

    class Config:
        orm_mode = True
