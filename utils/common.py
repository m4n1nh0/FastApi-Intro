import secrets
import string

from fastapi import HTTPException


def secret_key_generator() -> str:
    """Random string generator."""
    generate = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(generate) for _ in range(50))
    return secret_key


def http_exception(message, status, headers=None) -> HTTPException:
    """Error message."""
    return HTTPException(
        status_code=status,
        detail=message,
        headers=headers
    )
