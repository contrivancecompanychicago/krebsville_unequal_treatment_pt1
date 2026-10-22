from __future__ import annotations

from fastapi import FastAPI

from app.config import settings
from app.db import init_db
from app.routes import router as game_router

app = FastAPI(title=settings.app_name, version="0.1.0")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


app.include_router(game_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Krebsville backend is running. Visit /docs for the API."}
