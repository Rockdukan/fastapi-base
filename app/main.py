from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.lifespan import lifespan


def create_app() -> FastAPI:
    """Собирает и возвращает экземпляр FastAPI.

    Returns:
        Настроенное приложение.
    """

    settings = get_settings()
    app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
    app.include_router(api_router)

    return app


app = create_app()
