"""Login schemas implementation."""

from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    """Login schema."""

    username: EmailStr
    password: str
