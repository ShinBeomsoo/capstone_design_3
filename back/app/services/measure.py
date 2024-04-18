from typing import List, Optional
from sqlalchemy.orm import Session

from app.model.measure import MeasureInfoModel
from app.repositories.measure import MeasureRepo


class MeasureService:
    def __init__(self, measure_repo: MeasureRepo) -> None:
        self.measure_repo = measure_repo

    async def get_measure_info(self, info_id: int, db: Session) -> MeasureInfoModel:
        return await self.measure_repo.get_measure_info(info_id, db)

    async def get_measure_info_list(self, db: Session) -> List[MeasureInfoModel]:
        return await self.measure_repo.get_measure_info_list(db)
