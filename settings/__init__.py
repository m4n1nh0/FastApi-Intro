from pathlib import Path

from fastapi.security import HTTPBearer
from prettyconf import config

from utils.common import secret_key_generator

# Variable to sign the JWT token.
SECRET_KEY = config("SECRET_KEY", default=secret_key_generator())

# Variable to sign the JWT token.
ALGORITHM = "HS256"

# Variable that will contain the token expiration time.
ACCESS_TOKEN_EXPIRE_MINUTES = int(config(
    "ACCESS_TOKEN_EXPIRE_MINUTES", default="60"))

# SYSTEM SETTINGS
OPENAPI_URL = config("OPEN_API_URL", default=None)
RE_DOC_URL = config("REDOC", default=None)
DOCS_URL = config("DOCS", default=None)

# Instantiating Bearer class functions
security = HTTPBearer()

# local root folder address.
ROOT_DIR = Path(__file__).parent.parent

# Get the origins of requests.
allow_origins = config("ALLOW_ORIGINS", default=None)

if "," in allow_origins:
    allow_origins = allow_origins.split(",")
else:
    allow_origins = [allow_origins]