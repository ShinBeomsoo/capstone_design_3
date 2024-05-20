import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

import os


# load .env
load_dotenv()


ENDPOINT = os.environ["AWS_RDS_ENDPOINT"]
PW = os.environ["AWS_RDS_PW"]
USER = os.environ["AWS_RDS_USER"]
DB_NAME = os.environ["AWS_RDS_DB"]

# CSV 파일 읽기
df = pd.read_csv("./normal_restaurant.csv")

# MySQL 데이터베이스에 연결 (여기서 'username', 'password', 'database_name'을 자신의 정보로 바꿔주세요)
engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PW}@{ENDPOINT}/{DB_NAME}"
    # host=ENDPOINT, user=USER, password=PW, database="sesame_bot", port=3306
)
# restaurant, mobum, measure

# DataFrame을 SQL 테이블로 저장 (여기서 'table_name'을 원하는 테이블 이름으로 바꿔주세요)
df.to_sql("restaurant", con=engine, if_exists="replace", index=False)
