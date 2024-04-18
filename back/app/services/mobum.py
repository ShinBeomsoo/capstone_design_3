from typing import List
from sqlalchemy.orm import Session

from app.model.mobum import MobumModel
from app.repositories.mobum import MobumRepo


class MobumService:
    def __init__(self, mobum_repo: MobumRepo) -> None:
        self.mobum_repo = mobum_repo

    async def get_mobum_check(self, db: Session) -> MobumModel:
        return await self.mobum_repo.get_mobum_check(db)
    
    async def get_mobum_list(self, db: Session) -> List[MobumModel]:
        return await self.mobum_repo.get_mobum_list(db)
