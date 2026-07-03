import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.logging_config import setup_logging

setup_logging()

logger = logging.getLogger("kubepilot")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts and stops.
    """

    logger.info("=" * 60)
    logger.info("Starting KubePilot AI...")
    logger.info("=" * 60)

    yield

    logger.info("=" * 60)
    logger.info("Stopping KubePilot AI...")
    logger.info("=" * 60)

app = FastAPI(
    title="KubePilot AI",
    description="Local AI Assistant for Docker & Kubernetes using LangChain + Ollama",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  
app.include_router(chat_router)

@app.get("/", tags=["Home"])
async def root():
    """
    Root endpoint.
    """

    return {
        "application": "KubePilot AI",
        "version": "1.0.0",
        "status": "Running",
        "llm": "Ollama",
        "framework": "FastAPI",
        "documentation": "/docs",
    }

@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "application": "KubePilot AI",
    }

logger.info("KubePilot AI initialized successfully.")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
