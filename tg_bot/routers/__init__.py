__all__ = ("router",)

from aiogram import F, Router

from .commands import router as commands_router
from .common import router as common_router
from tg_bot.handlers.wildberries import router as wildberries_router

router = Router(name=__name__)
router.message.filter(F.chat.type == "private")

router.include_routers(
    commands_router,
    wildberries_router,
)

# this one has to be the last!
router.include_router(common_router)
