import asyncio

from app.repositories.restraurant_gangnam import RestaurantGangnamRepo



class RestaurantGangnam:
    def __init__(self, restaurant_gangnam_repo: RestaurantGangnamRepo):
        self.restaurant_gangnam_repo = restaurant_gangnam_repo

    @staticmethod
    async def get_restaurant(self):
        restaurant_gangnam = self.restaurant_gangnam_repo.get_restaurant_gangnam()
        return restaurant_gangnam
