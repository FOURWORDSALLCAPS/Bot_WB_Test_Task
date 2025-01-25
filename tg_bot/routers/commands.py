from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot.utilities.message_editor import one_message_editor

router = Router(name=__name__)


@router.message(Command('start'))
async def start(message: types.Message) -> None:
    text = 'Чтобы получить данные по товару, нажмите кнопку ниже и укажите артикул'
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Получить данные по товару", callback_data="get_product")],
    ])
    await one_message_editor(event=message, text=text, reply_markup=keyboard)


@router.callback_query(F.data == "start")
async def start(callback: types.CallbackQuery) -> None:
    text = 'Чтобы получить данные по товару, нажмите кнопку ниже и укажите артикул'
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Получить данные по товару", callback_data="get_product")],
    ])
    await one_message_editor(event=callback, text=text, reply_markup=keyboard)
