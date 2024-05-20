
from dotenv import load_dotenv
import mysql.connector

import os

# load .env
load_dotenv()

ENDPOINT = os.environ["AWS_RDS_ENDPOINT"]
PW = os.environ["AWS_RDS_PW"]
USER = os.environ["AWS_RDS_USER"]
DB_NAME = os.environ["AWS_RDS_DB"]

connection = mysql.connector.connect(
    host=ENDPOINT,
    user=USER,
    password=PW,
    database=DB_NAME
)
print(connection)
# 커서 생성
cursor = connection.cursor()

try:
    # 특정 테이블의 특정 열을 읽어오기
    cursor.execute("SELECT id, 소재지지번 FROM measure_info")

    # 결과 가져오기
    rows = cursor.fetchall()

    # 가져온 데이터를 순회하며 계산 후 업데이트
    for row in rows:
        user_id, addr = row
        updated_addr = addr + "addr"  # 예시로 소재지지번 + "addr"
        print(user_id, updated_addr)
        # 업데이트 쿼리 실행
        cursor.execute("UPDATE measure_info SET 소재지지번 = %s WHERE id = %s", (updated_addr, user_id))
    # 변경사항 저장
    connection.commit()

    print("업데이트 완료")

except mysql.connector.Error as error:
    print("MySQL 에러: {}".format(error))

finally:
    # 리소스 정리
    cursor.close()
    connection.close()