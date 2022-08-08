from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from api import models
from api.db.base import SessionLocal


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_item_by_id(item_id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).get(item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
