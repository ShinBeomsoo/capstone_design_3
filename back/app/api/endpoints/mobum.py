from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.mobum import Mobum
from app.services.mobum import MobumService
from dependencies import get_db, get_mobum


router = APIRouter()


@router.get(
    path="",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=Mobum,
)
async def mobum1(
    service: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> Mobum:
    mobum = await service.get_mobum_check(db)
    return mobum
