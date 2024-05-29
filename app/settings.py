from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URL: PostgresDsn


settings = Settings()
