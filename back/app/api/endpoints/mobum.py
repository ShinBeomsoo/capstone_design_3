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
    name: Annotated[str | None, Query()] = None,
    gu: Annotated[str | None, Query()] = None,
    type: Annotated[str | None, Query()] = None,
    best: Annotated[str | None, Query()] = None,
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> list[Mobum]:
    mobum = await service.get_mobum_list(name, gu, type, best, db)
    return mobum


@router.get(
    path="/{mobum_id}",
    summary="특정 모범음식점의 데이터를 가져옵니다.",
    description="특정 모범음식점 데이터를 가져옵니다.",
    response_description="특정 모범 음식점 데이터를 가져옵니다.",
    response_model=MobumDetail,
)
async def mobum_detail(
    mobum_id: Annotated[int, Path(gt=0)],
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> list[Mobum]:
    mobum = await service.get_mobum_detail(mobum_id, db)
    return mobum
