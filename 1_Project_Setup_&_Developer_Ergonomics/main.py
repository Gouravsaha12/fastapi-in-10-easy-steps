
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI 10 Steps",
    version="0.1.0",
)

@app.get("/health", tags=["health"])
def health_check():
    """
    A simple endpoint to verify the service is running.
    """
    return {"status": "ok"}
