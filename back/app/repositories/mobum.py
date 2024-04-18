from typing import List, Optional
from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.mobum import MobumModel


class MobumRepo:
    def __init__(self) -> None:
        pass

    async def get_mobum_detail(mobum_id: int, db: Session) -> Optional[MobumModel]:
        try:
            mobum = db.query(MobumModel).filter(MobumModel.id == mobum_id).first()
            return mobum
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")

    async def get_mobum_list(db: Session) -> List[MobumModel]:
        try:
            mobum = db.query(MobumModel).all()
            return mobum
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
