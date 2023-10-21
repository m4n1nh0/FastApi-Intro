"""""FastApi Configuration"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT

from database.redis import redis_conn
from settings import allow_origins, DOCS_URL, RE_DOC_URL, OPENAPI_URL
from settings.jwt_auth import AuthJwtSettings
from settings.openapi import class_openapi


@AuthJWT.load_config
def get_config():
    """JWT Token Configuration."""
    return AuthJwtSettings()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    """JWT Verification if token exists in denylist."""
    jti = decrypted_token['jti']
    entry = redis_conn.get(jti)
    return entry and entry == 'true'


def create_app() -> FastAPI:
    """"FastApi interface."""
    app = FastAPI(
        docs_url=DOCS_URL,
        redoc_url=RE_DOC_URL,
        openapi_url=OPENAPI_URL
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.openapi = class_openapi(app)

    from routers import user, login

    app.include_router(user.router)
    app.include_router(login.router)

    return app
