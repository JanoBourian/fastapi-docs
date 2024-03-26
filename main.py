from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import random

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"Hello": "world"}

@app.get("/items/{item_id}")
async def read_item(item_id:int, q: str | None = None, p: int | None = None) -> dict:
    value = random.randrange(10)
    await asyncio.sleep(value)
    return {"item_id": item_id, "q" : q, "p": p, "value": value}

@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item) -> dict:
    return {"item_name": item.name, "item_id": item_id}