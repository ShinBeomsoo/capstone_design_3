from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.measure import MeasureInfo
from app.services.measure import MeasureService
from dependencies import get_db, get_measure


router = APIRouter()


@router.get(
    path="/check",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=MeasureInfo,
)
async def measure_info_check(
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> MeasureInfo:
    info = await service.get_measure_info(1, db)
    return info


@router.get(
    path="/",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=List[MeasureInfo],
)
async def measure_info_list(
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> List[MeasureInfo]:
    info = await service.get_measure_info_list(db)
    return info


@router.get(
    path="/{info_id}",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=MeasureInfo,
)
async def measure_info_detail(
    info_id: int,
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> MeasureInfo:
    info = await service.get_measure_info(info_id, db)
    return info
