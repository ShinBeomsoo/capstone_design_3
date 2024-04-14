from datetime import datetime
from pydantic import BaseModel


class TestModel(BaseModel):
    id: int = 1
    지정번호: str = "지정번호"
    지정일자: datetime = datetime.now()
    업소명: str = "업소명"
    소재지지번: str = "소재지지번"
    업태명: str = "업태명"
    주된음식: str = "주된음식"
