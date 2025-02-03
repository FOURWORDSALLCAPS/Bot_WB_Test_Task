# Bot for collecting data on Wildberry products

FastAPI with a bot on Aiogram for collecting data on products from Wildberry. The data is stored in PostgreSQL, and APScheduler is used to periodically update the information. The service is loaded into Docker and launched via docker-compose.

## Functionality

### API

POST /api/v1/products
```json
{
"article": 211695539
}
```

GET /api/v1/subscribe/{artikul}

Data source: `GET https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}`

## Authorization

### Bearer
(optional) Endpoints can be protected with a Bearer token.

## Bot

"Get product data" button

The user enters the article, the bot sends the latest saved data on the product.


# Python version
I was using Python `3.13.1`.

# Author
(2025) Vladimir Zaitsev

