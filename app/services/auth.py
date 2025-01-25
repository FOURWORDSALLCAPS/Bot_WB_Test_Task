from http import HTTPStatus

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.schemes import Token

from app.settings import settings

oauth2_scheme_user = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login/')


class AuthService:
    def __init__(self):
        self.access_token: int = settings.ACCESS_TOKEN
        self.access_user: int = settings.ACCESS_USER
        self.access_password: int = settings.ACCESS_PASSWORD

    def check_token(self, token: Token):
        if token != self.access_token:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail='Could not validate credentials',
                headers={'WWW-Authenticate': 'Bearer'},
            )

    async def authenticate_user(self, user_data: OAuth2PasswordRequestForm):
        username = user_data.username
        password = user_data.password

        if username != self.access_user and password != self.access_password:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='Incorrect username or password')

        return Token(
            access_token=user_data.client_id,
        )

def checking_credentials(
    token: Token = Depends(oauth2_scheme_user),
    auth_service: AuthService = Depends(),
):
    return auth_service.check_token(token)
