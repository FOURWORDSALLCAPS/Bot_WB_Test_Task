from http import HTTPStatus

from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from app.dependencies import container
from app.repositories import WildberriesRepository
from app.engines.wb_api_client import WBApiClientEngine
from app.schemes import WBProductSearchParameters, WBProductResponse, WBProduct


class WBProductService:
    def __init__(self):
        self.wildberries_repository: WildberriesRepository = container.resolve(WildberriesRepository)
        self.scheduler: AsyncIOScheduler = container.resolve(AsyncIOScheduler)

    async def get_wildberries_products(
        self,
        search_params: WBProductSearchParameters,
    ) -> WBProductResponse:
        article = search_params.article
        products = await self.__fetch_products_by_article(article)
        is_created = await self.__create_product_from_db(products, article)
        if not is_created:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Can not create product.',
            )
        return await self.wildberries_repository.get_product(article)

    async def get_wildberries_subscribe(
        self,
        search_params: WBProductSearchParameters,
    ):
        article = search_params.article
        await self.__fetch_products_by_article(article)
        self.scheduler.add_job(
            self.__scheduled_task,
            trigger=IntervalTrigger(minutes=1),
            args=[article],
            id=f'subscribe_{article}',
            replace_existing=True
        )
        return JSONResponse(status_code=200, content={"message": "Subscription successful"})

    async def __scheduled_task(self, article: str):
        products = await self.__fetch_products_by_article(article)
        await self.__create_product_from_db(products, article)

    @staticmethod
    async def __fetch_products_by_article(article: str) -> list:
        async with WBApiClientEngine() as client:
            response = await client.get_products(article)
            products = response.json().get('data', {}).get('products', [])
            if not products:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Product with: {article} not found.',
                )
            return products

    async def __create_product_from_db(self, products: list, article: str) -> WBProduct:
        product = products[0]
        sale_price = round(product['salePriceU'] / 100)
        new_product = WBProduct(
            name=product['name'],
            article=article,
            sale_price=sale_price,
            rating=product['rating'],
            total_quantity=product['totalQuantity'],
        )
        return await self.wildberries_repository.create_product(new_product.model_dump())
