from typing import Optional
from fastapi import HTTPException
from pymysql import OperationalError
from app.model.restaurant_gangnam import RestaurantGangnamModel
from sqlalchemy.orm import Session


class RestaurantGangnamRepo:
    def __init__(self) -> None:
        pass

    async def get_restaurant_gangnam(db: Session) -> Optional[RestaurantGangnamModel]:
        try:
            restaurant_gangnam = db.query(RestaurantGangnamModel).filter(RestaurantGangnamModel.id == 1).first()
            return restaurant_gangnam
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
