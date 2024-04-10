from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings


settings = get_settings()
DB_URL = f"""mysql+pymysql://{settings.USER}:{settings.PW}@{settings.HOST}:3306/{settings.DB_NAME}"""

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
