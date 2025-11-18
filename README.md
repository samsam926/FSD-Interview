# 📘 Task – Full Stack Application

## Overview
Create a small full‑stack app (frontend + backend) and package it with Docker. The frontend displays a table/list populated from the backend. The backend reads CSV/Excel from disk, converts to JSON, exposes a minimal CRUD API.

---

## Features (requirements)
- Frontend
    - Single page that displays a table or list
    - Starts empty, fetches data from backend, populates the UI
- Backend (Python 3)
    - Use FastAPI or Flask
    - At least one API endpoint
    - Read CSV/Excel from disk and convert to JSON
    - Provide basic CRUD: list, create, delete (minimum)
- Docker
    - Dockerfile to build and run the app

---

## Tech stack (suggested)
- Backend: Python 3 + FastAPI (or Flask)
- Frontend: React / Vue / Angular / Vanilla JS
- Data: CSV or Excel on disk
- Container: Docker

---

## Project structure (suggested)
- backend/
    - app.py (FastAPI/Flask)
    - requirements.txt
    - data/
        - data.csv (or data.xlsx)
- frontend/
    - src/
    - package.json
- Dockerfile
- README.MD

---

## API (example)
- GET  /api/items         -> list items (reads CSV/Excel, returns JSON)
- POST /api/items         -> create item (append to CSV or write storage)
- DELETE /api/items/{id}  -> delete item

Request/response format: JSON arrays/objects. Document fields according to CSV columns.

---

## Setup & run (local)
Backend (example with FastAPI)
1. Create virtual env: `python -m venv .venv && source .venv/bin/activate`
2. Install: `pip install -r backend/requirements.txt`
3. Run: `uvicorn backend.app:app --reload --port 8000`

Frontend (example)
1. `cd frontend`
2. `npm install`
3. `npm run dev` (or `npm start`)

Open frontend in browser and ensure it calls `http://localhost:8000/api/items`.

---

## Build & run with Docker
1. Build: `docker build -t fsd-interview .`
2. Run: `docker run -p 8000:8000 fsd-interview`

Adjust Dockerfile to start both frontend and backend (or use multi-stage / docker-compose).

---

## Data handling notes
- Keep a canonical CSV/Excel in `backend/data/`.
- For simple persistence, append to CSV on create and rewrite on delete.
- For concurrency or production, use a database.

---

## Tips
- Start with list endpoint first (GET) to confirm frontend receives JSON.
- Use CORS on backend when frontend runs on a different port.
- Add minimal validation for create/delete endpoints.

---