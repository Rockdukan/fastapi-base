from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.repositories import user as user_repository
from app.schemas.user import UserCreate, UserRead


async def register_user(session: AsyncSession, payload: UserCreate) -> UserRead:
    """
    Регистрирует нового пользователя.

    Args:
        session: Сессия БД.
        payload: Входные данные.

    Returns:
        DTO созданного пользователя.

    Raises:
        HTTPException: Если email уже занят.
    """
    existing = await user_repository.get_user_by_email(session, str(payload.email))

    if existing is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email уже занят")

    hashed = hash_password(payload.password)
    user = await user_repository.create_user(session, str(payload.email), hashed)

    return UserRead.model_validate(user)
