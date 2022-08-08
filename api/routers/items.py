from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api import schemas, models
from api.dependencies import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.Item])
async def read_items(
        db: Session = Depends(get_db),

):
    return db.query(models.Item).all()


@router.get("/{item_id}/", response_model=schemas.Item)
async def read_item(
        item_id: str,
        db: Session = Depends(get_db),

):
    return db.query(models.Item).get(item_id)


@router.patch(
    "/{item_id}/",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
    response_model=schemas.Item,
)
async def update_item(
        item_id: str,
        item: schemas.ItemToUpdate,
        db: Session = Depends(get_db),
):
    db_item = db.query(models.Item).get(item_id)
    data_to_update = item.dict(exclude_unset=True)
    for key, val in data_to_update.items():
        setattr(db_item, key, val)
    db.commit()
    # db.refresh(db_item)
    return db_item


@router.post("/", response_model=schemas.Item)
def create_item(
        item: schemas.ItemToCreate,
        db: Session = Depends(get_db),

):
    # db_item = models.Item(**item.dict(), owner_id=user_id)
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    # db.refresh(db_item) # redundancy
    return db_item
