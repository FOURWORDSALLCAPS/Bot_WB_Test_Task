import logging
import sys
from httpx import AsyncClient, AsyncHTTPTransport, ConnectError, Response

from app.settings import settings

log = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))
log.addHandler(stream_handler)

class WBApiClientEngine:
    def __init__(
        self,
        method: str = 'GET',
        url: str = 'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}',
    ) -> None:
        self.method = method
        self.url = url
        self.client = AsyncClient(transport=AsyncHTTPTransport())

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, *args):
        if self.client:
            await self.client.aclose()
            self.client = None

    async def get_products(self, article: str) -> Response | None:
        formatted_url = self.url.format(article=article)
        try:
            response = await self.client.request(self.method, formatted_url)
            response.raise_for_status()
            return response
        except ConnectError as err:
            log.error(msg=f'Connection error: {err}', exc_info=False)
            return None
        except Exception as e:
            log.error(msg=f'An error occurred: {e}', exc_info=True)
            return None
