from sqlalchemy.orm import Session

from app.model.mobum import MobumModel
from app.repositories.mobum import MobumRepo


class MobumService:
    def __init__(self, mobum_repo: MobumRepo) -> None:
        self.mobum_repo = mobum_repo

    async def get_mobum(self, db: Session) -> MobumModel:
        return await self.mobum_repo.get_mobum(db)
