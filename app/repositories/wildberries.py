from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert

from app.dependencies import container
from app.engines.postgres_storage import PostgresEngine

from app.models.wildberries import WildberriesProductDB


class WildberriesRepository:
    __slots__ = ('db', 'wildberries_product')

    def __init__(self):
        self.db: PostgresEngine = container.resolve(PostgresEngine)
        self.wildberries_product: str = 'wildberries_product'

    async def create_product(self, product: dict[str, int]):
        stmt = (
            insert(WildberriesProductDB)
            .values(**product)
            .on_conflict_do_update(
                index_elements=WildberriesProductDB.__table__.primary_key.columns,
                set_={**product, WildberriesProductDB.update_date: func.now()},
            )
            .returning(WildberriesProductDB)
        )
        result = await self.db.execute(stmt)  # noqa
        return result

    async def get_product(self, article: str):
        stmt = (
            select(WildberriesProductDB)
            .where(WildberriesProductDB.article == article)
        )
        result = await self.db.select_one(stmt)  # noqa
        return result
