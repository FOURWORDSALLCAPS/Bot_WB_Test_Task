from pydantic import BaseModel, Field


class WBProduct(BaseModel):
    name: str = Field(
        title='Название товара',
        description='Название товара',
        examples=['Леггинсы спортивные'],
    )
    article: str = Field(
        title='Артикул',
        description='Артикулу товара',
        examples=['243817280'],
    )
    sale_price: int = Field(
        title='Цена',
        description='Цена продажи',
        examples=['1070'],
    )
    rating: int = Field(
        title='Рейтинг',
        description='Рейтинг товара',
        examples=['5'],
    )
    total_quantity: int = Field(
        title='Кол. товара',
        description='Суммарное количество товара на всех складах на момент запроса',
        examples=['1642'],
    )


class WBProductResponse(WBProduct):
    pass


class WBProductSearchParameters(BaseModel):
    article: str = Field(
        title='Артикул',
        description='Артикулу товара с Wildberries',
        examples=['211695539'],
    )
