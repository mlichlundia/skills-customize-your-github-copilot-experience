import os
import sqlite3
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

DATABASE = "items.db"
app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemOut(Item):
    id: int


def init_db() -> None:
    conn = sqlite3.connect(DATABASE)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            in_stock INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def row_to_item(row: sqlite3.Row) -> ItemOut:
    return ItemOut(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        price=row["price"],
        in_stock=bool(row["in_stock"]),
    )


@app.on_event("startup")
def startup_event() -> None:
    if not os.path.exists(DATABASE):
        init_db()


@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to the FastAPI CRUD API with SQLite"}


@app.get("/items/", response_model=List[ItemOut])
def read_items(db: sqlite3.Connection = Depends(get_db)) -> List[ItemOut]:
    cursor = db.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    return [row_to_item(row) for row in rows]


@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int, db: sqlite3.Connection = Depends(get_db)) -> ItemOut:
    cursor = db.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return row_to_item(row)


@app.post("/items/", response_model=ItemOut, status_code=201)
def create_item(item: Item, db: sqlite3.Connection = Depends(get_db)) -> ItemOut:
    cursor = db.execute(
        "INSERT INTO items (name, description, price, in_stock) VALUES (?, ?, ?, ?)",
        (item.name, item.description, item.price, int(item.in_stock)),
    )
    db.commit()
    item_id = cursor.lastrowid
    return ItemOut(id=item_id, **item.dict())


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: Item, db: sqlite3.Connection = Depends(get_db)) -> ItemOut:
    cursor = db.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    if cursor.fetchone() is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.execute(
        "UPDATE items SET name = ?, description = ?, price = ?, in_stock = ? WHERE id = ?",
        (item.name, item.description, item.price, int(item.in_stock), item_id),
    )
    db.commit()
    return ItemOut(id=item_id, **item.dict())


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: sqlite3.Connection = Depends(get_db)) -> dict:
    cursor = db.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    if cursor.fetchone() is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.execute("DELETE FROM items WHERE id = ?", (item_id,))
    db.commit()
    return {"message": "Item deleted successfully"}
