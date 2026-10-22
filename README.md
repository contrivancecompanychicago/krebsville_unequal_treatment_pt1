# Krebsville Nights: Unequal Treatment

This repository is now structured as a playable game plus a lightweight backend starter.

## Repository layout

- `data/` — reusable game data and zone definitions
- `docs/` — game rules and lore
- `engine.js` — browser game logic
- `backend/` — FastAPI backend for game data and player records

## Backend starter

The backend reads from the existing `data/firebase_zones.json` and exposes the game as a JSON API.

### Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Example API requests

```bash
curl http://localhost:8000/api/overview
curl http://localhost:8000/api/zones
curl -X POST http://localhost:8000/api/players \
  -H "Content-Type: application/json" \
  -d '{"name":"Dr. Grant","time_tokens":39,"credits":3480,"hazard_level":0,"current_zone_id":1,"inventory":["Data Spike"]}'
```

## Next step ideas

- add authentication for player sessions
- add SQLAlchemy/Postgres persistence for production
- add a browser client that consumes the API
- add quizzing, quest endpoints, and world state transitions

## Original game context

This project started as a static landing page and interactive browser experience; the backend scaffold makes it reusable as an actual game data source and API-driven world.
