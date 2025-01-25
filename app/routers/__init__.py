from fastapi import APIRouter

from app.routers.wildberries import router as wildberries_router
from app.routers.auth import router as auth_router

from app.settings import settings

router = APIRouter(prefix='/api/v1', include_in_schema=settings.DEVELOP)
router.include_router(wildberries_router)
router.include_router(auth_router)
