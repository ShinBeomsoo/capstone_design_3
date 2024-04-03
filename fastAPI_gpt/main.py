import os
from fastapi import FastAPI, HTTPException
import httpx

from model.airquality import AirQualityResponse


app = FastAPI()

# 공공 데이터 미세먼지 API URL 및 필요한 파라미터 설정
# 시도별 실시간 측정정보 조회
PUBLIC_DATA_API_URL = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
API_KEY = os.environ["PUBLIC_DATA_API_KEY"]
SERVICE = "미세먼지 API"
SIDO_NAME = "충남"
VERSION = "1.0"

@app.get(
    path="/health",
    response_model=dict,
    summary="서비스 상태를 확인합니다.",
    description="서비스 상태를 확인합니다. 서비스가 정상적으로 동작하는지 확인할 때 사용합니다.",
    tags=["Health"],
)
async def main():
    return {"message": "health!"}

@app.get(
    path="/dust/choongnam",
    response_model=AirQualityResponse,
    summary="대한민국 충남시의 미세먼지 데이터를 제공합니다.",
    description="대한민국 충청남도의 CAI최종 실시간 측정값과 지수 정보 조회 기능을 제공하는 실시간 측정정보 조회",
    response_description="대한민국 충청남도의 대기질 정보를 제공합니다.",
    tags=[SERVICE],
)
async def get_dust(sidoname: str = "충남"):
    params = {
        "serviceKey": API_KEY,
        "sidoName": sidoname,
        "numOfRows": "1",  # 한 페이지 결과 수
        "pageNo": "1",  # 페이지 번호
        "ver": VERSION,
        "returnType": "json",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(PUBLIC_DATA_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="API 요청에 실패했습니다.")
        data = response.json()
        # 여기서는 응답에서 PM10 값을 추출하는 방법을 가정합니다. 실제 응답 구조에 따라 변경해야 할 수 있습니다.
    print("api calling")
    print("sidoname: ", sidoname)
    print(data['response'])
    return data['response']

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
