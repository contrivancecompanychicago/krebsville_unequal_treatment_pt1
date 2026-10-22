from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException

from app.config import settings
from app.data_store import get_zone_by_id, get_zone_catalog
from app.models import PlayerPayload, PlayerResponse
from app.db import create_player, get_player

router = APIRouter(prefix="/api", tags=["game"])


@router.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }


@router.get("/zones")
def list_zones() -> list[dict[str, Any]]:
    return get_zone_catalog()


@router.get("/zones/{zone_id}")
def get_zone(zone_id: int) -> dict[str, Any]:
    zone = get_zone_by_id(zone_id)
    if zone is None:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone


@router.get("/players/{player_id}")
def fetch_player(player_id: str) -> PlayerResponse:
    player = get_player(player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return PlayerResponse(
        player_id=player.player_id,
        name=player.name,
        time_tokens=player.time_tokens,
        credits=player.credits,
        hazard_level=player.hazard_level,
        current_zone_id=player.current_zone_id,
        inventory=player.inventory,
    )


@router.post("/players", status_code=201)
def register_player(payload: PlayerPayload) -> PlayerResponse:
    player = create_player(payload)
    return PlayerResponse(
        player_id=player.player_id,
        name=player.name,
        time_tokens=player.time_tokens,
        credits=player.credits,
        hazard_level=player.hazard_level,
        current_zone_id=player.current_zone_id,
        inventory=player.inventory,
    )


@router.get("/overview")
def overview() -> dict[str, Any]:
    return {
        "game": "Krebsville Nights: Unequal Treatment",
        "zone_count": len(get_zone_catalog()),
        "default_starting_zone": 1,
        "starting_time_tokens": 39,
        "starting_credits": 3480,
        "starting_hazard_level": 0,
    }
