from app.db.database import SessionLocal


# def get_mobum() -> MobumService:
#     return MobumService(mobum_repo=MobumRepo)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
