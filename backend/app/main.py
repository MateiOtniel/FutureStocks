import os

from fastapi import FastAPI
from .api.endpoints import linear_regression

app = FastAPI()

app.include_router(linear_regression.router, prefix="/linear_regression", tags=["linear_regression"])

@app.get("/")
async def root():
    return {"message": "Hello World"}