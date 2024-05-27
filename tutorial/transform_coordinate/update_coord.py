from dotenv import load_dotenv
import mysql.connector

import os
from pyproj import CRS, Transformer

epsg5174_proj = CRS("+proj=tmerc +lat_0=38 +lon_0=127.0028902777778 +k=1 +x_0=200000 +y_0=500000 +ellps=bessel +units=m +no_defs +towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43")
wgs84_proj = CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")

transformer = Transformer.from_crs(epsg5174_proj, wgs84_proj)
# load .env
load_dotenv(dotenv_path="../../.env")

ENDPOINT = os.environ["AWS_RDS_ENDPOINT"]
PW = os.environ["AWS_RDS_PW"]
USER = os.environ["AWS_RDS_USER"]
DB_NAME = os.environ["AWS_RDS_DB"]

connection = mysql.connector.connect(
    host=ENDPOINT, user=USER, password=PW, database=DB_NAME, autocommit=False
)
print(connection)
# 커서 생성
cursor = connection.cursor()
try:
    # 특정 테이블의 특정 열을 읽어오기
    cursor.execute("SELECT id, 좌표정보_X, 좌표정보_Y, 영업상태명 FROM restaurant")

    # 결과 가져오기
    rows = cursor.fetchall()

    # 가져온 데이터를 순회하며 계산 후 업데이트
    for row in rows:
        index, x, y, status = row
        if x == None or y == None or status == "폐업":
            continue
        longtitude, latitude = transformer.transform(x, y)
        # print(index, longtitude, latitude)
        cursor.execute(f"UPDATE restaurant SET 위도 = {latitude}, 경도 = {longtitude} WHERE id = {index}")
    # raise/
    # 변경사항 저장
    connection.commit()

    print("업데이트 완료")

except mysql.connector.Error as error:
    print("MySQL 에러: {}".format(error))

finally:
    # 리소스 정리
    cursor.close()
    connection.close()
