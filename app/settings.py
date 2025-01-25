from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEVELOP: bool = False
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8900
    TITLE: str = 'API'
    VERSION: str = 'v1.0'
    DOC_URL: str = '/docs'
    OPENAPI_URL: str = '/openapi.json'
    LOG_LEVEL: str = 'debug'
    LOG_FORMAT: str = (
        '{"time": "%(asctime)s", "level": "%(levelname)s", "file": "%(name)s", "line": "%(lineno)s", "msg": "%(msg)s"}'
    )
    POSTGRES_URI: str = 'postgresql+asyncpg://postgres_user:postgres_password@postgres:5432/postgres_database'
    POSTGRES_POOL_SIZE: int = 20
    POSTGRES_MAX_OVERFLOW: int = 5
    WORKERS: int = 1
    ACCESS_TOKEN: str = ''
    ACCESS_USER: str = 'admin'
    ACCESS_PASSWORD: str = 'admin'


settings = Settings(
    _env_file='./../.env',
    _env_file_encoding='utf-8',
)
