from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    """
    Возвращает пользователя по email.

    Args:
        session: Сессия БД.
        email: Адрес электронной почты.

    Returns:
        Экземпляр `User` или `None`.
    """
    result = await session.execute(select(User).where(User.email == email))

    return result.scalar_one_or_none()



async def create_user(session: AsyncSession, email: str, hashed_password: str) -> User:
    """
    Создаёт пользователя.

    Args:
        session: Сессия БД.
        email: Email.
        hashed_password: Хэш пароля.

    Returns:
        Сохранённый пользователь.
    """
    user = User(email=email, hashed_password=hashed_password)
    session.add(user)
    await session.flush()
    await session.refresh(user)

    return user
