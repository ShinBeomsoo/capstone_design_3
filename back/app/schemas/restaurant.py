from datetime import datetime
from pydantic import BaseModel


class Restaurant(BaseModel):
    id: int = 0
    관리번호: str = "관리번호"
    사업장명: str = "사업장명"
    지번주소: str = "지번주소"
    업태구분명: str = "업태구분명"
    좌표정보_X: float | None = "좌표정보_X"
    좌표정보_Y: float | None = "좌표정보_Y"


class RestaurantDetail(Restaurant):
    인허가일자: datetime = "인허가일자"
    전화번호: str | None = "전화번호"
    도로명주소: str | None = "도로명주소"
