from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import get_settings
from app.db.base import Base

engine: AsyncEngine | None = None
session_factory: async_sessionmaker[AsyncSession] | None = None


async def init_engine() -> None:
    """Создаёт глобальный async engine и sessionmaker."""
    global engine, session_factory

    settings = get_settings()
    engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)
    session_factory = async_sessionmaker(engine, expire_on_commit=False, autoflush=False)

    if settings.DEBUG:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


async def close_engine() -> None:
    """Закрывает пул соединений движка."""
    global engine, session_factory

    if engine is not None:
        await engine.dispose()

    engine = None
    session_factory = None


async def get_session() -> AsyncIterator[AsyncSession]:
    """
    Поставляет сессию БД для зависимостей FastAPI.

    Yields:
        Открытая асинхронная сессия.

    Raises:
        RuntimeError: Если `init_engine` ещё не вызывался.
    """
    if session_factory is None:
        raise RuntimeError("session_factory не инициализирован; проверьте lifespan.")

    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
