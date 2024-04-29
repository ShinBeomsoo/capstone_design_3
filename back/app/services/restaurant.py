from typing import List
from sqlalchemy.orm import Session

from app.model.restaurant import RestaurantModel
from app.repositories.restaurant import RestaurantRepo


class RestaurantService:
    def __init__(self, restaurant_repo: RestaurantRepo) -> None:
        self.restaurant_repo = restaurant_repo

    async def get_restaurant_detail(
        self, restaurant_id: int, db: Session
    ) -> RestaurantModel:
        return await self.restaurant_repo.get_restaurant_detail(restaurant_id, db)

    async def get_restaurant_list(
        self,
        name: str | None,
        gu: str | None,
        restaurantType: str | None,
        db: Session,
    ) -> List[RestaurantModel]:
        return await self.restaurant_repo.get_restaurant_list(
            name, gu, restaurantType, db
        )
