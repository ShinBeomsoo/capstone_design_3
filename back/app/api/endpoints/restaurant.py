from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.restaurant_gangnam import RestaurantGangnam
from dependencies import get_db, get_restaurant_gangnam

# from app.schemas.health import Health


router = APIRouter()


@router.get(
    path="/gangnam",
    summary="강남구에 있는 모범음식점 데이터를 가져옵니다.",
    description="",
    response_description="",
    response_model=dict,
)
async def get_restaurant(
    restaurant_gangnam: RestaurantGangnam = Depends(get_restaurant_gangnam),
    db: Session = Depends(get_db)
):
    await restaurant_gangnam.get_restaurant(db)
    return {"result": "success"}
