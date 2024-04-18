from typing import List, Optional
from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.measure import MeasureInfoModel


class MeasureRepo:
    def __init__(self) -> None:
        pass

    async def get_measure_info(info_id: int, db: Session) -> Optional[MeasureInfoModel]:
        try:
            info = (
                db.query(MeasureInfoModel)
                .filter(MeasureInfoModel.id == info_id)
                .first()
            )
            return info
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
