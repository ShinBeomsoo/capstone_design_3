from typing import Optional
from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.mobum import MobumModel


class MobumRepo:
    def __init__(self) -> None:
        pass

    async def get_mobum(db: Session) -> Optional[MobumModel]:
        try:
            mobum = db.query(MobumModel).filter(MobumModel.지정번호 == "0160").first()
            return mobum
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")