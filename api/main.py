"""
source: https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases
"""
from fastapi import FastAPI

from api.db.base import engine, Base
from api.routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)
