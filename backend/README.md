# Krebsville Nights backend starter

This repository now includes a small FastAPI backend scaffold under `backend/` that exposes the game data and player state as an API.

## Quick start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Routes

- `GET /` — service health
- `GET /api/health` — backend health check
- `GET /api/overview` — game metadata
- `GET /api/zones` — list all game zones from `data/firebase_zones.json`
- `GET /api/zones/{zone_id}` — fetch one zone
- `POST /api/players` — create a player record
- `GET /api/players/{player_id}` — fetch player state

## Data model

The app reads the existing zone catalog from `data/firebase_zones.json` and stores player state in a SQLite database at `backend/krebsville.db` by default.

## Why this is useful

This creates a reusable backend source for gamers and clients to query the world state without depending on a static GitHub Pages front end. It is a good base for future API integrations, dashboards, or a multiplayer game server.
