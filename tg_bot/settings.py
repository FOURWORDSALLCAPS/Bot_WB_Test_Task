from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str = ''
    LOG_FORMAT: str = (
        '{"time": "%(asctime)s", "level": "%(levelname)s", "file": "%(name)s", "line": "%(lineno)s", "msg": "%(msg)s"}'
    )
    APP_URI: str = 'http://app:8000/api/v1/products/'
    ACCESS_TOKEN: str = ''

settings = Settings(
    _env_file='./../.env',
    _env_file_encoding='utf-8',
)
