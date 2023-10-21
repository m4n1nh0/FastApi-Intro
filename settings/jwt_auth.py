"""JWT AUTH schemas implementation."""

from pydantic import BaseModel

from settings import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM


class AuthJwtSettings(BaseModel):
    """Settings schema."""

    authjwt_secret_key: str = SECRET_KEY
    authjwt_algorithm: str = ALGORITHM
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access", "refresh"}
    authjwt_access_token_expires: int = ACCESS_TOKEN_EXPIRE_MINUTES
    authjwt_refresh_token_expires: int = ACCESS_TOKEN_EXPIRE_MINUTES + 1800
