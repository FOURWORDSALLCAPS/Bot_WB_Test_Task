from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot.utilities.message_editor import one_message_editor

router = Router(name=__name__)


@router.message()
async def echo_message(message: types.Message) -> None:
    text = 'Чтобы получить данные по товару, нажмите кнопку ниже и укажите артикул'
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Получить данные по товару", callback_data="get_product")],
    ])
    await one_message_editor(event=message, text=text, reply_markup=keyboard)
