from aiogram.fsm.state import State, StatesGroup


class ProductState(StatesGroup):
    article = State()
