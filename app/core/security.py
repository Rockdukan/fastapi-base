from datetime import UTC, datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from app.core.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Хэширует пароль для хранения.

    Args:
        password: Открытый пароль.

    Returns:
        Строка хэша.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверяет пароль против хэша.

    Args:
        plain_password: Открытый пароль.
        hashed_password: Сохранённый хэш.

    Returns:
        `True`, если пароль совпадает.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    """
    Создаёт подписанный JWT access-токен.

    Args:
        subject: Идентификатор субъекта (например, email или user id).
        expires_delta: Явный TTL; если не задан — из настроек.

    Returns:
        Закодированная строка JWT.
    """
    settings = get_settings()

    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = datetime.now(tz=UTC) + expires_delta
    payload: dict[str, Any] = {"sub": subject, "exp": expire}

    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_access_token(token: str) -> dict[str, Any]:
    """
    Декодирует JWT и возвращает полезную нагрузку.

    Args:
        token: Строка JWT.

    Returns:
        Словарь claims.

    Raises:
        JWTError: Если токен недействителен.
    """
    settings = get_settings()

    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
