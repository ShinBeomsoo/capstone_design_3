from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.measure import MeasureData, MeasureInfo
from app.services.measure import MeasureService
from dependencies import get_db, get_measure


router = APIRouter()


@router.get(
    path="/info/check",
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
    path="/info",
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
    path="/info/{info_id}",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=MeasureInfo,
)
async def measure_info(
    info_id: int,
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> MeasureInfo:
    info = await service.get_measure_info(info_id, db)
    return info


@router.get(
    path="/data/check",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=List[MeasureData],
)
async def measure_data_check(
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> List[MeasureData]:
    info = await service.get_measure_data(18990105006, db)
    return info


@router.get(
    path="/data/{issuance_num}",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=List[MeasureData],
)
async def measure_data(
    issuance_num: int,
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> List[MeasureData]:
    info = await service.get_measure_data(issuance_num, db)
    return info
