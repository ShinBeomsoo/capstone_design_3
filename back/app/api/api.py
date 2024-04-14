from fastapi import APIRouter

from app.api.endpoints import health, mobum
from app.api.endpoints import restaurant


api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(restaurant.router, prefix="/restaurant", tags=["restaurant"])
api_router.include_router(mobum.router, prefix="/mobum", tags=["mobum"])
