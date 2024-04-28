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
    response_description="음식점 리스트를 가져옵니다.",
    response_model=list[Restaurant],
)
async def restaurant_list(
    name: Annotated[
        str | None,
        Query(
            title="업소명",
            description="일치하는 업소명을 가진 음식점의 데이터를 가져옵니다. 예) 이도곰탕",
        ),
    ] = None,
    gu: Annotated[
        str | None,
        Query(
            title="구",
            description="일치하는 구를 가진 음식점의 데이터를 가져옵니다. 예) 강남구",
        ),
    ] = None,
    type: Annotated[
        str | None,
        Query(
            title="업종",
            description="일치하는 업종을 가진 음식점의 데이터를 가져옵니다. 예) 한식",
        ),
    ] = None,
    service: RestaurantService = Depends(get_restaurant),
    db: Session = Depends(get_db),
) -> list[Restaurant]:
    restaurant = await service.get_restaurant_list(name, gu, type, db)
    return restaurant


@router.get(
    path="/{restaurant_id}",
    summary="특정 음식점의 데이터를 가져옵니다.",
    description="특정 음식점 데이터를 가져옵니다.",
    response_description="특정 음식점의 세부 데이터를 가져옵니다.",
    response_model=RestaurantDetail,
)
async def restaurant_detail(
    restaurant_id: Annotated[
        int,
        Path(
            title="음식점 식별 아이디",
            description="특정 아이디 값을 가진 음식점의 세부 정보를 가져옵니다. 예) 1",
            gt=0,
        ),
    ],
    service: RestaurantService = Depends(get_restaurant),
    db: Session = Depends(get_db),
) -> RestaurantDetail:
    restaurant = await service.get_restaurant_detail(restaurant_id, db)
    return restaurant
