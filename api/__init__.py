from fastapi import APIRouter

from api.health.health import health_router
from api.thinking.thinking import think_router

from core.config import config

router = APIRouter(prefix=config.api_prefix)

router.include_router(health_router, tags=['Health'])
router.include_router(think_router, tags=['Thinking'])

__all__ = ["router"]
