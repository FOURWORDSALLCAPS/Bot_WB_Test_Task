import asyncio
import logging

from aiogram import Dispatcher
from aiogram.exceptions import TelegramNetworkError

from tg_bot.base import bot
from tg_bot.routers import router


async def main():
    logger = logging.getLogger('Tg')
    logger.info("Starting bot")

    dp = Dispatcher()
    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    except TelegramNetworkError:
        logging.critical('Нет интернета')


if __name__ == '__main__':
    asyncio.run(main())
