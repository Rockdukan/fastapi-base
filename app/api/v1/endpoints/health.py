from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", summary="Healthcheck")
async def health() -> dict[str, str]:
    """
    Возвращает статус приложения.

    Returns:
        Словарь со статусом.
    """
    return {"status": "ok"}
