from fastapi import HTTPException
from pymysql import OperationalError
from app.model.restaurant_gangnam import RestaurantGangnamModel


class RestaurantGangnamRepo:
    def __init__(self) -> None:
        pass

    @staticmethod
    async def get_restaurant_gangnam(user_id: str):
        try:
            return await RestaurantGangnamModel.all()
        except OperationalError as e:
            raise HTTPException(detail=f"{e} 가입이 안되어 있는 유저입니다.")
