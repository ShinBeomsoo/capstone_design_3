from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.mobum import TestModel
from app.services.mobum import MobumService
from dependencies import get_db, get_mobum


router = APIRouter()

@router.get(
    path="",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=TestModel,
)
async def mobum1(
    mobum: MobumService = Depends(get_mobum),
    db: Session = Depends(get_db),
) -> TestModel:
    mobum = await mobum.get_mobum(db)
    return mobum