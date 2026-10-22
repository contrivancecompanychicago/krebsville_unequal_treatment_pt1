from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from app.config import settings


@lru_cache(maxsize=1)
def get_zone_catalog() -> list[dict]:
    path = Path(settings.zone_data_path)
    if not path.exists():
        raise FileNotFoundError(f"Zone data file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        zones = json.load(f)

    return [
        {
            "id": zone.get("id"),
            "zone_key": zone.get("zone_key"),
            "name": zone.get("name"),
            "status": zone.get("status"),
            "hazard_level": zone.get("hazard_level"),
            "active_npc": zone.get("active_npc"),
            "specialist_assigned": zone.get("specialist_assigned"),
            "access_requirement": zone.get("access_requirement"),
            "scene_data": zone.get("scene_data", {}),
            "inventory_state": zone.get("inventory_state"),
            "interactables": zone.get("interactables"),
            "objectives": zone.get("objectives"),
            "created_at": zone.get("created_at"),
        }
        for zone in zones
    ]


def get_zone_by_id(zone_id: int) -> dict | None:
    for zone in get_zone_catalog():
        if zone["id"] == zone_id:
            return zone
    return None
