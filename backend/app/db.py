from __future__ import annotations

import json
from typing import Any

from sqlmodel import Field, Session, SQLModel, create_engine, select

from app.config import settings
from app.models import PlayerPayload

DATABASE_URL = settings.database_url
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)


class Player(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    player_id: str = Field(index=True, unique=True)
    name: str
    time_tokens: int = 39
    credits: int = 3480
    hazard_level: int = 0
    current_zone_id: int = 1
    inventory: str = "[]"


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def create_player(payload: PlayerPayload) -> Player:
    from uuid import uuid4

    player = Player(
        player_id=str(uuid4()),
        name=payload.name,
        time_tokens=payload.time_tokens,
        credits=payload.credits,
        hazard_level=payload.hazard_level,
        current_zone_id=payload.current_zone_id,
        inventory=json.dumps(payload.inventory or []),
    )

    with Session(engine) as session:
        session.add(player)
        session.commit()
        session.refresh(player)
        return player


def get_player(player_id: str) -> Player | None:
    with Session(engine) as session:
        return session.exec(select(Player).where(Player.player_id == player_id)).first()
