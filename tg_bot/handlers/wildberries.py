from textwrap import dedent

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot.utilities.message_editor import one_message_editor
from tg_bot.state import ProductState
from tg_bot.facades import AppFacade

router = Router(name=__name__)


@router.callback_query(F.data == "get_product")
async def get_article(callback: types.CallbackQuery, state: FSMContext) -> None:
    text = 'Укажите артикул товара'
    await state.set_state(ProductState.article)
    await one_message_editor(event=callback, text=text)


@router.message(ProductState.article)
async def get_product(message: types.Message, state: FSMContext):
    await state.update_data(article=message.text)
    user_message = await state.get_data()
    article = user_message.get('article')
    async with AppFacade() as client:
        response = await client.get_products(article)
    if not response:
        text = f'По данному артикулу: {article} товар не найден! Попробуйте указать другой'
        await state.set_state(ProductState.article)
        await one_message_editor(event=message, text=text)
        return
    product = response.json()
    text = f'''
        ·Название товара: {product.get('name')}
        ·Артикул: {product.get('article')}
        ·Цена: {product.get('sale_price')}
        ·Рейтинг товара: {product.get('rating')}
        ·Суммарное количество товара: {product.get('total_quantity')}
    '''
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="start")],
    ])
    await one_message_editor(event=message, text=dedent(text), reply_markup=keyboard)
