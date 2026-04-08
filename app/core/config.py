from functools import lru_cache
from pathlib import Path

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
    SECRET_KEY: str = "change-me-in-production"
    DATABASE_URL: str = "sqlite+aiosqlite:///./db.sqlite3"
    ALEMBIC_DATABASE_URL: str = "sqlite:///./db.sqlite3"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


@lru_cache
def get_settings() -> Settings:
    """
    Возвращает закэшированный экземпляр настроек.

    Returns:
        Экземпляр `Settings`.
    """
    return Settings()


def resolve_database_path() -> Path:
    """
    Извлекает путь к файлу SQLite из URL для Alembic и проверок.

    Returns:
        Абсолютный путь к файлу базы.

    Notes:
        Предполагается формат `sqlite:///relative/path` или `sqlite+aiosqlite:///...`.
    """
    settings = get_settings()
    raw = settings.ALEMBIC_DATABASE_URL.replace("sqlite:///", "", 1)

    return Path(raw).resolve()
