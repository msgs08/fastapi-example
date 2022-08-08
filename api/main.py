"""
source: https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases
"""

from fastapi import FastAPI

# from api.models import users
from api.db.base import engine
from api.routers import users, items

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)
# app.include_router(users.router)
