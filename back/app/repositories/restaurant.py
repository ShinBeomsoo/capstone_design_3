from fastapi import HTTPException
from pymysql import OperationalError
from sqlalchemy.orm import Session

from app.model.restaurant import RestaurantModel


class RestaurantRepo:
    def __init__(self) -> None:
        pass

    async def get_restaurant_detail(
        restaurant_id: int, db: Session
    ) -> RestaurantModel | None:
        try:
            restaurant = (
                db.query(RestaurantModel)
                .filter(RestaurantModel.id == restaurant_id)
                .first()
            )
            return restaurant
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")

    async def get_restaurant_list(
        name: str | None, gu: str | None, restaurantType: str | None, db: Session
    ) -> list[RestaurantModel]:
        try:
            restaurant = db.query(RestaurantModel)
            if name:
                restaurant = restaurant.filter_by(사업장명=name)
            if gu:
                restaurant = restaurant.filter(RestaurantModel.지번주소.like(f"%{gu}%"))
            if restaurantType:
                restaurant = restaurant.filter_by(업태구분명=restaurantType)
            return restaurant.all()
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
