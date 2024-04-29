from fastapi import APIRouter

from app.api.endpoints import gpt, health
from app.api.endpoints import restaurant
from app.api.endpoints import mobum
from app.api.endpoints import measure


api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health", "check"])
api_router.include_router(restaurant.router, prefix="/restaurants", tags=["restaurant"])
api_router.include_router(mobum.router, prefix="/mobums", tags=["mobum"])
api_router.include_router(measure.router, prefix="/measures", tags=["measure"])
api_router.include_router(gpt.router, prefix="/gpt", tags=["gpt"])