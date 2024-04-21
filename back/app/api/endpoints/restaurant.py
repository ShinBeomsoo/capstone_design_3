from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.restaurant import Restaurant, RestaurantDetail
from app.services.restaurant import RestaurantService
from dependencies import get_db, get_restaurant


router = APIRouter()


@router.get(
    path="",
    summary="저장된 모든 음식점 데이터를 가져옵니다.",
    description="저장된 모든 음식점 데이터를 가져옵니다.",
    response_description="음식점 리스트",
    response_model=List[Restaurant],
)
async def restaurant_list(
    name: str | None = None,
    gu: str | None = None,
    type: str | None = None,
    service: RestaurantService = Depends(get_restaurant),
    db: Session = Depends(get_db),
) -> List[Restaurant]:
    restaurant = await service.get_restaurant_list(name, gu, type, db)
    return restaurant


@router.get(
    path="/{restaurant_id}",
    summary="특정 모범음식점의 데이터를 가져옵니다.",
    description="특정 모범음식점 데이터를 가져옵니다.",
    response_description="특정 모범 음식점 데이터를 가져옵니다.",
    response_model=RestaurantDetail,
)
async def restaurant_detail(
    restaurant_id: int,
    service: RestaurantService = Depends(get_restaurant),
    db: Session = Depends(get_db),
) -> List[RestaurantDetail]:
    restaurant = await service.get_restaurant_detail(restaurant_id, db)
    return restaurant
