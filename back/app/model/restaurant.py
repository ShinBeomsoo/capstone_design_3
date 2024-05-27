from sqlalchemy import DECIMAL, Column, TEXT, INT, DateTime, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RestaurantModel(Base):
    __tablename__ = "restaurant"

    id = Column(INT, primary_key=True, autoincrement=True)
    관리번호 = Column(TEXT, nullable=True, default=null)
    사업장명 = Column(TEXT, nullable=True, default=null)
    지번주소 = Column(TEXT, nullable=True, default=null)
    업태구분명 = Column(TEXT, nullable=True, default=null)
    위도 = Column(DECIMAL, nullable=True, default=null)
    경도 = Column(DECIMAL, nullable=True, default=null)
    인허가일자 = Column(DateTime, nullable=True, default=null)
    전화번호 = Column(TEXT, nullable=True, default=null)
    도로명주소 = Column(TEXT, nullable=True, default=null)
