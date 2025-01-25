from fastapi import APIRouter, Depends

from app.schemes import WBProductResponse, WBProductSearchParameters
from app.services import WBProductService
from app.services.auth import checking_credentials

router = APIRouter(tags=['Wildberries'])


@router.post('/products/', response_model=WBProductResponse)
async def get_wildberries_products(
    search_params: WBProductSearchParameters,
    wb_product_service: WBProductService = Depends(),
    current_credentials: str = Depends(checking_credentials),
):
    return await wb_product_service.get_wildberries_products(
        search_params=search_params,
    )


@router.get('/subscribe/', response_model=WBProductResponse)
async def get_wildberries_subscribe(
    search_params: WBProductSearchParameters = Depends(),
    wb_product_service: WBProductService = Depends(),
    current_credentials: str = Depends(checking_credentials),
):
    return await wb_product_service.get_wildberries_subscribe(
        search_params=search_params,
    )
