from typing import List, Optional
from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.restaurant import RestaurantModel


class RestaurantRepo:
    def __init__(self) -> None:
        pass

    async def get_restaurant_detail(
        restaurant_id: int, db: Session
    ) -> Optional[RestaurantModel]:
        try:
            restaurant = (
                db.query(RestaurantModel)
                .filter(RestaurantModel.id == restaurant_id)
                .first()
            )
            return restaurant
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")

    async def get_restaurant_list(db: Session) -> List[RestaurantModel]:
        try:
            restaurant = db.query(RestaurantModel).all()
            return restaurant
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
