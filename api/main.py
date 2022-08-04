"""
source: https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases
"""

from fastapi import FastAPI

from api.orm import models
from api.orm.db import engine
from api.routers import users, items

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
