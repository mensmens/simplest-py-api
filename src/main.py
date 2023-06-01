"""
Simplest Py API
---------------
A simple API to deploy for testing or similar
"""
from fastapi import FastAPI
import uvicorn


app: FastAPI = FastAPI(
    title="Simplest Py API",
    description="A simple API to deploy for testing or similar",
    version="1.0"
)


@app.get("/", tags=["Root"])
async def root() -> str:
    return "Simplest Py API is running"


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)
