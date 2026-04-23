from fastapi import APIRouter
from src.contexts.campaigns.api.routers.health_router import router as health_router

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["health"])
