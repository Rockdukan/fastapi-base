from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.session import close_engine, init_engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Открывает и закрывает ресурсы на время работы приложения.

    Args:
        app: Экземпляр FastAPI-приложения.

    Yields:
        Управление после инициализации.
    """
    await init_engine()

    yield

    await close_engine()
