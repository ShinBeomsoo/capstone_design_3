from app.db.database import SessionLocal
from app.repositories.mobum import MobumRepo
from app.services.mobum import MobumService


def get_mobum() -> MobumService:
    return MobumService(mobum_repo=MobumRepo)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
