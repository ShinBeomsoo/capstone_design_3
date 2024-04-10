from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.restaurant_gangnam import RestaurantGangnam

# from app.schemas.health import Health


router = APIRouter()


@router.get(
    path="/gangnam",
    summary="강남구에 있는 모범음식점 데이터를 가져옵니다.",
    description="",
    response_description="",
    response_model=None,
)
async def get_restaurant(
    db: Session = Depends(get_db)
) -> None:
    
    return {"Hello": "World"}
