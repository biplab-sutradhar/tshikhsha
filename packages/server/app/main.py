"""
This module contains the FastAPI application for the server.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return a welcome message."""
    return {"message": "Hello, World!"}
