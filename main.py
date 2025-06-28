from datetime import datetime
import time
import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator

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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
