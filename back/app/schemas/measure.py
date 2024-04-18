from datetime import datetime
from pydantic import BaseModel

class MeasureInfo(BaseModel):
    교부번호: int = "교부번호"
    업소명: str = "업소명"
    소재지지번: str = "소재지지번"

class MeasureData(BaseModel):
    id: int = 0
    처분일자: datetime = datetime.now()
    행정처분상태: str = "행정처분상태"
    처분명: str = "처분명"
    법적근거: str = "법적근거"
    위반일자: datetime = datetime.now()
    위반내용: str = "위반내용"
    처분내용: str = "처분내용"
    처분기간: float | None = 0