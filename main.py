""""Setup file."""

import uvicorn

from settings.fastapi_app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, server_header=False)
