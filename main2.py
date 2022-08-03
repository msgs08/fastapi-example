import datetime
from enum import Enum
from typing import Union, Set

from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic.main import BaseModel
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


class Tags(Enum):
    items = "items"
    exceptions = "exceptions"


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.get("/items/{item_id}", tags=[Tags.items])
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    tags=[Tags.items],
)
async def create_item(item: Item):
    return item


@app.post(
    "/items_desc/",
    response_model=Item,
    summary="Create an item",
    response_description="The created Item object",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/exceptions/{name}", tags=[Tags.exceptions])
async def read_unicorn(name: str):
    if name == "foo":
        raise UnicornException(name=name)
    return {"name": name}


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]


@app.get("/jsonable_obj/")
async def read_elements():
    return jsonable_encoder({"dt": datetime.datetime.utcnow()})
