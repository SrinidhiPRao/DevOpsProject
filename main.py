from datetime import datetime
import time
import logging
from typing import Dict
from uuid import uuid4

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.exceptions import HTTPException

# In-memory note store
notes_db: Dict[str, Dict] = {}


class NoteCreate(BaseModel):
    title: str
    content: str


class Note(NoteCreate):
    id: str
    timestamp: str


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(filename="/app/logs/app.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Learning FastAPI with Observability",
    description="A simple FastAPI app for learning Loki, Grafana, and Prometheus integration",
    version="1.0.0",
)


Instrumentator().instrument(app).expose(app)


@app.get("/")
async def home():
    """Home endpoint that returns a simple greeting"""
    start_time = time.time()

    logger.info("Home endpoint accessed")

    response_data = {
        "message": "Welcome to FastAPI Observability Learning!",
        "timestamp": datetime.now().isoformat(),
        "status": "healthy",
    }

    # Log response time for monitoring
    response_time = time.time() - start_time
    logger.info(f"Home endpoint responded in {response_time:.4f} seconds")

    return JSONResponse(content=response_data)


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    logger.info("Health check endpoint accessed")

    return JSONResponse(
        content={
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "service": "fastapi-observability-app",
        }
    )


@app.get("/notes")
async def get_notes():
    start_time = time.time()
    logger.info("List all notes endpoint accessed")

    response = list(notes_db.values())

    duration = time.time() - start_time
    logger.info(f"Listed {len(response)} notes in {duration:.4f} seconds")
    return JSONResponse(content=response)


@app.post("/notes")
async def create_note(note: NoteCreate):
    start_time = time.time()
    logger.info("Create note endpoint accessed")

    note_id = str(uuid4())
    new_note = {
        "id": note_id,
        "title": note.title,
        "content": note.content,
        "timestamp": datetime.now().isoformat(),
    }
    notes_db[note_id] = new_note

    duration = time.time() - start_time
    logger.info(f"Note {note_id} created in {duration:.4f} seconds")
    return JSONResponse(status_code=201, content=new_note)


@app.get("/notes/{note_id}")
async def read_note(note_id: str):
    start_time = time.time()
    logger.info(f"Read note endpoint accessed for ID: {note_id}")

    note = notes_db.get(note_id)
    if not note:
        logger.warning(f"Note {note_id} not found")
        raise HTTPException(status_code=404, detail="Note not found")

    duration = time.time() - start_time
    logger.info(f"Note {note_id} fetched in {duration:.4f} seconds")
    return JSONResponse(content=note)


@app.put("/notes/{note_id}")
async def update_note(note_id: str, updated: NoteCreate):
    start_time = time.time()
    logger.info(f"Update note endpoint accessed for ID: {note_id}")

    if note_id not in notes_db:
        logger.warning(f"Note {note_id} not found for update")
        raise HTTPException(status_code=404, detail="Note not found")

    notes_db[note_id].update(
        {
            "title": updated.title,
            "content": updated.content,
            "timestamp": datetime.now().isoformat(),
        }
    )

    duration = time.time() - start_time
    logger.info(f"Note {note_id} updated in {duration:.4f} seconds")
    return JSONResponse(content=notes_db[note_id])


@app.delete("/notes/{note_id}")
async def delete_note(note_id: str):
    start_time = time.time()
    logger.info(f"Delete note endpoint accessed for ID: {note_id}")

    if note_id not in notes_db:
        logger.warning(f"Note {note_id} not found for deletion")
        raise HTTPException(status_code=404, detail="Note not found")

    deleted_note = notes_db.pop(note_id)

    duration = time.time() - start_time
    logger.info(f"Note {note_id} deleted in {duration:.4f} seconds")
    return JSONResponse(content={"message": "Note deleted", "note": deleted_note})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
