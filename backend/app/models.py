from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class ZoneSummary(BaseModel):
    id: int
    zone_key: str
    name: str
    status: str
    hazard_level: int
    active_npc: Optional[str] = None
    specialist_assigned: Optional[str] = None
    access_requirement: Optional[str] = None


class PlayerPayload(BaseModel):
    name: str
    time_tokens: int = 39
    credits: int = 3480
    hazard_level: int = 0
    current_zone_id: int = 1
    inventory: list[str] | None = None


class PlayerResponse(BaseModel):
    player_id: str
    name: str
    time_tokens: int
    credits: int
    hazard_level: int
    current_zone_id: int
    inventory: list[str]
