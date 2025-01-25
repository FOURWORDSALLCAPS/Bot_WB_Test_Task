from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemes import Token
from app.services import AuthService

router = APIRouter(prefix='/auth', tags=['Authorization'])


@router.post('/login/', response_model=Token)
async def user_login(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
) -> Token:
    return await auth_service.authenticate_user(
        user_data=auth_data,
    )
