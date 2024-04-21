from typing import List, Optional
from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.measure import MeasureModel


class MeasureRepo:
    def __init__(self) -> None:
        pass

    async def get_measure_list(q: str, db: Session) -> List[MeasureModel]:
        try:
            measure = db.query(MeasureModel).filter(MeasureModel.업소명 == q).all()
            return measure
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
