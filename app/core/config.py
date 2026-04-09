from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Конфигурация, загружаемая из переменных окружения и файла `.env`."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "fastapi-base"
    DEBUG: bool = False


@lru_cache
def get_settings() -> Settings:
    """
    Возвращает закэшированный экземпляр настроек.

    Returns:
        Экземпляр `Settings`.
    """
    return Settings()
