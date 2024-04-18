from typing import List, Optional
from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.measure import MeasureDataModel, MeasureInfoModel


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

    async def get_measure_info_list(db: Session) -> List[MeasureInfoModel]:
        try:
            info = db.query(MeasureInfoModel).all()
            return info
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")

    async def get_measure_data(
        issuance_num: int, db: Session
    ) -> List[MeasureDataModel]:
        try:
            data = (
                db.query(MeasureDataModel)
                .filter(MeasureDataModel.교부번호 == issuance_num)
                .all()
            )
            return data
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
