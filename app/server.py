from typing import List
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from api import router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Example App on FastAPI",
        description="Example API",
        version="0.1.0",
        docs_url="/docs",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()

@app.get('/')
async def main():
    with open(os.path.join(os.path.dirname(__file__), '../templates/index.html'), 'r') as f:
        s = f.read()
    return HTMLResponse(s)
