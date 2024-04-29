from sqlalchemy import Column, TEXT, INT, DateTime, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MobumModel(Base):
    __tablename__ = "mobum"

    id = Column(INT, primary_key=True, autoincrement=True)
    지정번호 = Column(TEXT, nullable=True, default=null)
    지정일자 = Column(DateTime, nullable=True, default=null)
    업소명 = Column(TEXT, nullable=True, default=null)
    업태명 = Column(TEXT, nullable=True, default=null)
    소재지지번 = Column(TEXT, nullable=True, default=null)
    주된음식 = Column(TEXT, nullable=True, default=null)
