"""User schemas implementation."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserInsertSchema(BaseModel):
    """User insert schema."""

    usr_name: str
    username: EmailStr
    password: str

    class Config:
        """" Leitura de qualquer dado inicial do dicionario."""

        orm_mode = True


class UserUpdateSchema(BaseModel):
    """User insert schema."""

    usr_name: Optional[str]
    password: Optional[str]
    age: Optional[int]

    class Config:
        """" Leitura de qualquer dado inicial do dicionario."""

        orm_mode = True


class UserValuesSchema(BaseModel):
    """User insert schema."""

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    usr_name: str
    username: EmailStr
    age: Optional[int] = None

    class Config:
        """" Leitura de qualquer dado inicial do dicionario."""

        orm_mode = True


class UserResponse(BaseModel):
    users: list[UserValuesSchema]
