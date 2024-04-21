from sqlalchemy import BIGINT, DOUBLE, Column, TEXT, INT, DateTime, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MeasureModel(Base):
    __tablename__ = "measure"

    id = Column(INT, primary_key=True, autoincrement=True)
    처분일자 = Column(DateTime, nullable=True, default=null)
    업소명 = Column(TEXT, nullable=True, default=null)
    소재지지번 = Column(TEXT, nullable=True, default=null)
    교부번호 = Column(BIGINT, nullable=True, default=null)
    행정처분상태 = Column(TEXT, nullable=True, default=null)
    처분명 = Column(TEXT, nullable=True, default=null)
    법적근거 = Column(TEXT, nullable=True, default=null)
    위반일자 = Column(DateTime, nullable=True, default=null)
    위반내용 = Column(TEXT, nullable=True, default=null)
    처분내용 = Column(TEXT, nullable=True, default=null)
    처분기간 = Column(DOUBLE, nullable=True, default=null)
