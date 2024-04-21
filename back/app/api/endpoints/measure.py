from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas.measure import Measure
from app.services.measure import MeasureService
from dependencies import get_db, get_measure


router = APIRouter()


@router.get(
    path="/",
    summary="모범음식점 데이터를 가져옵니다.",
    description="모범음식점 데이터를 가져옵니다.",
    response_description="모범 음식점 데이터를 가져옵니다.",
    response_model=List[Measure],
)  # TODO: q의 default value = None으로 수정
async def measure_list(
    q: Annotated[str | None, Query()] = "삼성웨딩홀",
    service: MeasureService = Depends(get_measure),
    db: Session = Depends(get_db),
) -> List[Measure]:
    if q == None:
        raise HTTPException(status_code=400, detail="q is required")
    info = await service.get_measure_list(q, db)
    return info
