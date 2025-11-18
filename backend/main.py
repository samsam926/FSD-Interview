from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

import uvicorn

from backend import services

app = FastAPI()

# Base logic for items
items = []
next_id = 1


class Item(BaseModel):
    id: int
    name: str
    age: int


class ItemCreate(BaseModel):
    name: str
    age: int


app.include_router(services.router, tags=['Services'], prefix='/api/items')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
