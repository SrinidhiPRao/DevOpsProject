from datetime import datetime
import time

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Learning FastAPI with Observability",
    description="A simple FastAPI app for learning Loki, Grafana, and Prometheus integration",
    version="1.0.0",
)


@app.get("/")
async def home():
    """Home endpoint that returns a simple greeting"""
    start_time = time.time()

    response_data = {
        "message": "Welcome to FastAPI Observability Learning!",
        "timestamp": datetime.now().isoformat(),
        "status": "healthy",
    }

    response_time = time.time() - start_time

    return JSONResponse(content=response_data)


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""

    return JSONResponse(
        content={
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "service": "fastapi-observability-app",
        }
    )


if __name__ == "__main__":
    import uvicorn
    import multiprocessing

    multiprocessing.freeze_support()
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)
