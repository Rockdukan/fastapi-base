from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Общие поля пользователя."""
    email: EmailStr


class UserCreate(UserBase):
    """Данные для создания пользователя."""
    password: str = Field(min_length=8)


class UserRead(UserBase):
    """Пользователь, отдаваемый клиенту."""
    id: int

    model_config = {"from_attributes": True}
