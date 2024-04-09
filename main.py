from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import asyncio
import random

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
fake_names_db = [{"name": "John"}, {"name": "Carl"}, {"name": "Susan"}]

@app.get("/")
async def root() -> dict:
    return {"Hello": "world"}

@app.get("/testing/{number}")
async def testing(number:int, needy:str):
    return {"number": number, "needy": needy}

@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return {"result": {"item": random.choice(fake_items_db), "name": random.choice(fake_names_db)}}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None, p: int | None = None) -> dict:
    value = random.randrange(5)
    await asyncio.sleep(value)
    return {"item_id": item_id, "q": q, "p": p, "value": value}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item) -> dict:
    return {"item_name": item.name, "item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict:
    print(dir(model_name))
    message = "Have some residuals"
    if model_name is ModelName.alexnet:
        message = "Deep Learning WTF!"
    elif model_name.value == 'lenet':
        message = "LeCNN all the images"
    return {"model_name": model_name, "message": message}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str) -> dict:
    return {"file_path": file_path}

@app.get("/client/{client_id}/model/{model_id}")
async def get_model_by_client(client_id: int, model_id: int) -> dict:
    return {"client_id": client_id, "model_id": model_id}
