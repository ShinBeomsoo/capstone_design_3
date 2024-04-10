from typing import Any

import uvicorn

from app.core.config import get_settings
from app.api.api import api_router
from fastapi import FastAPI

from app.db.database import EngineConn


settings = get_settings()
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=f"이 문서는 {settings.PROJECT_NAME}을 구현하고자 API를 정리한 문서입니다.",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    root_path=settings.ROOT_PATH,
)
engine = EngineConn()
session = engine.session_maker()

# app.add_event_handler("startup", create_start_app_handler(app))
# app.add_event_handler("shutdown", create_shutdown_app_handler(app))

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.ALLOW_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
