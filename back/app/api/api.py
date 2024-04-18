from fastapi import APIRouter

from app.api.endpoints import health
from app.api.endpoints import mobum


api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health", "check"])
api_router.include_router(mobum.router, prefix="/mobums", tags=["mobum"])
