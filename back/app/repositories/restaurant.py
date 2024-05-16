from typing import List
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
            if restaurant is None:
                raise HTTPException(
                    status_code=404, detail="해당 음식점이 존재하지 않습니다."
                )
            return restaurant
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")

    async def get_restaurant_list(
        name: str | None, gu: str | None, restaurantType: str | None, db: Session
    ) -> List[RestaurantModel]:
        try:
            restaurant = db.query(RestaurantModel)
            if name:
                restaurant = restaurant.filter(
                    RestaurantModel.사업장명.like(f"%{name}%")
                )
            if gu:
                restaurant = restaurant.filter(RestaurantModel.지번주소.like(f"%{gu}%"))
            if restaurantType:
                restaurant = restaurant.filter_by(업태구분명=restaurantType)
            return restaurant.all()
        except OperationalError as e:
            print("error", e)
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
