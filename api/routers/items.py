"""
TODO: handle errors: 404
* response example
"""

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import schemas, models
from api.dependencies import get_db, get_item_by_id

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {
        "description": "Not found",
        "model": schemas.Item,  # TODO: dummy response model
    }},
)


@router.get("/", response_model=List[schemas.Item])
async def read_items(
        db: Session = Depends(get_db),

):
    return db.query(models.Item).all()


@router.get("/{item_id}/", response_model=schemas.Item)
async def read_item(
        db_item: models.Item = Depends(get_item_by_id),
):
    return db_item


@router.patch(
    "/{item_id}/",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
    response_model=schemas.Item,
)
async def update_item(
        request_item: schemas.ItemToUpdate,
        db_item: models.Item = Depends(get_item_by_id),
        db: Session = Depends(get_db),
):
    data_to_update = request_item.dict(exclude_unset=True)
    for key, val in data_to_update.items():
        setattr(db_item, key, val)
    db.commit()
    return db_item


# doc: https://fastapi.tiangolo.com/tutorial/response-status-code/#response-status-code
# doc: https://fastapi.tiangolo.com/advanced/response-change-status-code/
@router.post("/", response_model=schemas.Item, status_code=201)
def create_item(
        item: schemas.ItemToCreate,
        db: Session = Depends(get_db),

):
    # db_item = models.Item(**item.dict(), owner_id=user_id)
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    return db_item
