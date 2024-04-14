from app.db.database import SessionLocal
from app.repositories.mobum import MobumRepo
from app.repositories.restaurant_gangnam import RestaurantGangnamRepo
from app.services.mobum import MobumService
from app.services.restaurant_gangnam import RestaurantGangnam


def get_restaurant_gangnam() -> RestaurantGangnam:
    return RestaurantGangnam(restaurant_gangnam_repo=RestaurantGangnamRepo)

def get_mobum() -> MobumService:
    return MobumService(mobum_repo=MobumRepo)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
