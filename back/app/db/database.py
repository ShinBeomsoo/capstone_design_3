from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings


settings = get_settings()
DB_URL = f"""mysql+pymysql://
{settings.USER}:{settings.PW}@{settings.ENDPOINT}:3306/{settings.DB_NAME}
"""

class EngineConn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
    
    def session_maker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def conneciton(self):
        conn = self.engine.connect()
        return conn

def get_db():
    engine = EngineConn()
    session = engine.session_maker()
    try:
        yield session
    finally:
        session.close()
