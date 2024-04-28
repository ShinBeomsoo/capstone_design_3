from typing import Annotated

from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from app.schemas.mobum import Mobum, MobumDetail
from app.services.mobum import MobumService
from dependencies import get_db, get_mobum


router = APIRouter()


@router.get(
    path="",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=list[Mobum],
)
async def mobum_list(
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
    restaurantType: Annotated[
        str | None,
        Query(
            title="업종",
            description="일치하는 업종을 가진 음식점의 데이터를 가져옵니다. 예) 한식",
        ),
    ] = None,
    best_food: Annotated[
        str | None,
        Query(
            title="대표메뉴",
            description="일치하는 대표메뉴를 가진 음식점의 데이터를 가져옵니다. 예) 곰탕",
        ),
    ] = None,
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> list[Mobum]:
    mobum = await service.get_mobum_list(name, gu, restaurantType, best_food, db)
    return mobum


@router.get(
    path="/{mobum_id}",
    summary="특정 모범음식점의 데이터를 가져옵니다.",
    description="특정 모범음식점 데이터를 가져옵니다.",
    response_description="특정 모범 음식점의 세부 데이터를 가져옵니다.",
    response_model=MobumDetail,
)
async def mobum_detail(
    mobum_id: Annotated[
        int,
        Path(
            title="모범음식점 ID",
            description="특정 아이디를 가진 모범음식점의 데이터를 가져옵니다. 예) 1",
            gt=0,
        ),
    ],
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> list[Mobum]:
    mobum = await service.get_mobum_detail(mobum_id, db)
    return mobum
