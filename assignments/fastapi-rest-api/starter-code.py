from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = {
    1: {
        "name": "Sample Item",
        "description": "A starter item",
        "price": 9.99,
        "in_stock": True,
    }
}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI REST API"}

@app.get("/items/")
async def read_items():
    return {"items": items}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items[item_id]}

@app.post("/items/")
async def create_item(item: Item):
    new_id = max(items.keys(), default=0) + 1
    items[new_id] = item.dict()
    return {"item_id": new_id, "item": items[new_id]}
