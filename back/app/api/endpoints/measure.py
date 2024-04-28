from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas.measure import Measure
from app.services.measure import MeasureService
from dependencies import get_db, get_measure


router = APIRouter()


@router.get(
    path="/",
    summary="음식점 행정 처분 내역을 가져옵니다.",
    description="음식점 행정 처분 내역을 가져옵니다.",
    response_description="특정 업소명 가진 음식점의 행정 처분 내역 리스트",
    response_model=List[Measure],
)
async def measure_list(
    name: Annotated[
        str | None,
        Query(
            title="업소명",
            description="일치하는 업소명을 가진 음식점의 행정 처분 내역을 가져옵니다. 예) 삼성웨딩홀, 치어스",
        ),
    ] = None,
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> List[Measure]:
    if name == None:
        raise HTTPException(status_code=400, detail="q is required")
    info = await service.get_measure_list(name, db)
    return info
