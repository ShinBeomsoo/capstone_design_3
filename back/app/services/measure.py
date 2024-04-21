from typing import List, Optional
from sqlalchemy.orm import Session

from app.model.measure import MeasureModel
from app.repositories.measure import MeasureRepo
from app.schemas.measure import Measure


class MeasureService:
    def __init__(self, measure_repo: MeasureRepo) -> None:
        self.measure_repo = measure_repo

    async def get_measure_list(self, name: str, db: Session) -> List[MeasureModel]:
        return await self.measure_repo.get_measure_list(name, db)
