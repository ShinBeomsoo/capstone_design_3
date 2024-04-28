from typing import List
from sqlalchemy.orm import Session

from app.model.mobum import MobumModel
from app.repositories.mobum import MobumRepo


class MobumService:
    def __init__(self, mobum_repo: MobumRepo) -> None:
        self.mobum_repo = mobum_repo

    async def get_mobum_detail(self, mobum_id: int, db: Session) -> MobumModel:
        return await self.mobum_repo.get_mobum_detail(mobum_id, db)

    async def get_mobum_list(
        self,
        name: str | None,
        gu: str | None,
        restaurantType: str | None,
        best_food: str | None,
        db: Session,
    ) -> List[MobumModel]:
        return await self.mobum_repo.get_mobum_list(
            name, gu, restaurantType, best_food, db
        )
