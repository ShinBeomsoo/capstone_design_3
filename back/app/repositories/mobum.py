from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.mobum import MobumModel


class MobumRepo:
    def __init__(self) -> None:
        pass

    async def get_mobum_detail(mobum_id: int, db: Session) -> MobumModel | None:
        try:
            mobum = db.query(MobumModel).filter(MobumModel.id == mobum_id).first()
            return mobum
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")

    async def get_mobum_list(
        name: str | None,
        gu: str | None,
        type: str | None,
        best_food: str | None,
        db: Session,
    ) -> list[MobumModel]:
        try:
            mobum = db.query(MobumModel)
            if name:
                mobum = mobum.filter_by(업소명=name)
            if gu:
                mobum = mobum.filter(MobumModel.소재지지번.like(f"%{gu}%"))
            if type:
                mobum = mobum.filter_by(업태명=type)
            if best_food:
                mobum = mobum.filter_by(주된음식=best_food)
            return mobum
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
