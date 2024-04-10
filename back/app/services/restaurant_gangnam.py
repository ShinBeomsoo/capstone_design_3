from app.repositories.restaurant_gangnam import RestaurantGangnamRepo
from sqlalchemy.orm import Session


class RestaurantGangnam:
    def __init__(self, restaurant_gangnam_repo: RestaurantGangnamRepo) -> None:
        self.restaurant_gangnam_repo = restaurant_gangnam_repo

    async def get_restaurant(self, db: Session):
        await self.restaurant_gangnam_repo.get_restaurant_gangnam(db)
