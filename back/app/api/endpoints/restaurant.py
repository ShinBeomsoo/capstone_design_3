from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
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
    response_model=list[Restaurant],
)
async def restaurant_list(
    name: Annotated[str | None, Query()] = None,
    gu: Annotated[str | None, Query()] = None,
    type: Annotated[str | None, Query()] = None,
    service: RestaurantService = Depends(get_restaurant),
    db: Session = Depends(get_db),
) -> list[Restaurant]:
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
    restaurant_id: Annotated[int, Path(gt=0)],
    service: RestaurantService = Depends(get_restaurant),
    db: Session = Depends(get_db),
) -> RestaurantDetail:
    restaurant = await service.get_restaurant_detail(restaurant_id, db)
    return restaurant
