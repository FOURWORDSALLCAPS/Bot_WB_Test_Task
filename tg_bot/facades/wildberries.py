import logging
import sys

from httpx import AsyncClient, AsyncHTTPTransport, ConnectError, Response

from tg_bot.settings import settings

log = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))
log.addHandler(stream_handler)


class AppFacade:
    def __init__(
        self,
        method: str = 'POST',
        url: str = settings.APP_URI,
        token: str = settings.ACCESS_TOKEN
    ) -> None:
        self.method = method
        self.url = url
        self.token = token
        self.client = AsyncClient(transport=AsyncHTTPTransport())

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, *args):
        if self.client:
            await self.client.aclose()
            self.client = None

    async def get_products(self, article: str) -> Response | None:
        try:
            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'Authorization': f'Bearer {self.token}',
            }
            json = {
                'article': article,
            }
            response = await self.client.request(self.method, self.url, headers=headers, json=json)
            response.raise_for_status()
            return response
        except ConnectError as err:
            log.error(msg=f'Connection error: {err}', exc_info=False)
            return None
        except Exception as e:
            log.error(msg=f'An error occurred: {e}', exc_info=True)
            return None
