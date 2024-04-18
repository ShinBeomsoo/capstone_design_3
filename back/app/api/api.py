from fastapi import APIRouter

from app.api.endpoints import health
from app.api.endpoints import restaurant
from app.api.endpoints import mobum
from app.api.endpoints import measure


api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health", "check"])
api_router.include_router(restaurant.router, prefix="/restaurants", tags=["rastaurant"])
api_router.include_router(mobum.router, prefix="/mobums", tags=["mobum"])
api_router.include_router(measure.router, prefix="/measures", tags=["measure"])
