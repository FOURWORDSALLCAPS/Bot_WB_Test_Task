from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.dependencies import container
from app.engines import PostgresEngine, WBApiClientEngine
from app.repositories import WildberriesRepository
from app.routers import router
from app.settings import settings


def init_container(scheduler: AsyncIOScheduler) -> None:
    container.add_instance(PostgresEngine())
    container.add_instance(WBApiClientEngine())

    container.add_scoped(WildberriesRepository)
    container.add_instance(scheduler)


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    scheduler = AsyncIOScheduler()
    scheduler.start()
    init_container(scheduler)

    yield

    scheduler.shutdown()


app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    docs_url=settings.DOC_URL,
    openapi_url=settings.OPENAPI_URL,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware, # noqa
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOG_LEVEL,
        reload=settings.DEVELOP,
    )
