from sqlalchemy import Column, TEXT, INT, BIGINT, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RestaurantGangnamModel(Base):
    __tablename__ = "gangnam_restaurant"

    id = Column(INT, primary_key=True, autoincrement=True)
    시군구코드 = Column(BIGINT, nullable=True, default=null)
    지정년도 = Column(BIGINT, nullable=True, default=null)
    지정번호 = Column(BIGINT, nullable=True, default=null)
    신청일자 = Column(BIGINT, nullable=True, default=null)
    지정일자 = Column(BIGINT, nullable=True, default=null)
    업소명 = Column(TEXT, nullable=True, default=null)
    소재지도로명 = Column(TEXT, nullable=True, default=null)
    소재지지번 = Column(TEXT, nullable=True, default=null)
    업태명 = Column(TEXT, nullable=True, default=null)
    주된음식 = Column(TEXT, nullable=True, default=null)
    행정동명 = Column(TEXT, nullable=True, default=null)
    급수시설구분 = Column(TEXT, nullable=True, default=null)
    소재지전화번호 = Column(TEXT, nullable=True, default=null)
