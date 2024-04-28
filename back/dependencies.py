from app.db.database import SessionLocal
=
from app.repositories.mobum import MobumRepo
from app.services.mobum import MobumService
from app.repositories.measure import MeasureRepo
from app.services.measure import MeasureService
from app.repositories.restaurant import RestaurantRepo
from app.services.restaurant import RestaurantService


def get_restaurant() -> RestaurantService:
    return RestaurantService(restaurant_repo=RestaurantRepo)


def get_mobum() -> MobumService:
    return MobumService(mobum_repo=MobumRepo)


def get_measure() -> MeasureService:
    return MeasureService(measure_repo=MeasureRepo)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
