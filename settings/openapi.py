""""Open api configuration"""

import inspect
import re

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute


def class_openapi(app: FastAPI):
    """
    Custom configuration to openAPI schema.

    OpenAPI scheme generation to routers from FastAPI application
    """

    def openapi_generation():
        """"Swagger and bearer settings."""

        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title="Introdução a FastApi",
            version="0.0.1",
            description="Vamos conhecer esteuniverso",
            routes=app.routes
        )

        # Applying the bearer to the required token routes
        if "components" in openapi_schema:
            # Applying the bearer to the required token routes
            openapi_schema["components"]["securitySchemes"] = {
                "Bearer Auth": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "Authorization",
                    "description": "Enter: **'Bearer &lt;JWT&gt;'**, "
                                   "where JWT is the access token"
                }
            }

        # Get all routes where jwt_optional() or jwt_required
        api_router = [route for route in app.routes if
                      isinstance(route, APIRoute)]

        for route in api_router:
            path = getattr(route, "path")
            endpoint = getattr(route, "endpoint")
            methods = [
                method.lower() for method in getattr(route, "methods")]

            for method in methods:
                # access_token
                required = re.search(
                    "jwt_required", inspect.getsource(endpoint))

                refresh = re.search(
                    "jwt_refresh_token_required", inspect.getsource(endpoint))

                optional = re.search(
                    "jwt_optional", inspect.getsource(endpoint))

                if path in openapi_schema[
                        "paths"] and required or refresh or optional:
                    openapi_schema["paths"][path][method]["security"] = [
                        {
                            "Bearer Auth": []
                        }
                    ]

        app.openapi_schema = openapi_schema

        return app.openapi_schema

    return openapi_generation
