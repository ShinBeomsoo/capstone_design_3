from typing import Optional, List
from pydantic import BaseModel

# 'items' 리스트 내의 객체에 대한 모델
class Item(BaseModel):
    so2Grade: str
    coFlag: Optional[str] = None
    khaiValue: Optional[str] = None
    so2Value: Optional[str] = None
    coValue: Optional[str] = None
    pm25Flag: Optional[str] = None
    pm10Flag: Optional[str] = None
    o3Grade: Optional[str] = None
    pm10Value: Optional[str] = None
    khaiGrade: Optional[str] = None
    pm25Value: Optional[str] = None
    sidoName: Optional[str] = None
    no2Flag: Optional[str] = None
    no2Grade: Optional[str] = None
    o3Flag: Optional[str] = None
    pm25Grade: Optional[str] = None
    so2Flag: Optional[str] = None
    dataTime: Optional[str] = None
    coGrade: Optional[str] = None
    no2Value: Optional[str] = None
    stationName: Optional[str] = None
    pm10Grade: Optional[str] = None
    o3Value: Optional[str] = None

# 'body' 객체에 대한 모델
class Body(BaseModel):
    totalCount: int
    items: List[Item]
    pageNo: int
    numOfRows: int

# 'header' 객체에 대한 모델
class Header(BaseModel):
    resultMsg: str
    resultCode: str

# 최상위 객체에 대한 모델
class AirQualityResponse(BaseModel):
    # reponse: dict = {
    #     "body": Body,
    #     "header": Header
    # }
    body: Body
    header: Header