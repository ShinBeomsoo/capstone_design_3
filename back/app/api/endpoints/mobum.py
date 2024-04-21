from typing import Any, List

from fastapi import APIRouter, Depends
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
    response_model=List[Mobum],
)
async def mobum_list(
    name: str | None = None,
    gu: str | None = None,
    type: str | None = None,
    best: str | None = None,
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> List[Mobum]:
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
    mobum_id: int,
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> List[Mobum]:
    mobum = await service.get_mobum_detail(mobum_id, db)
    return mobum
