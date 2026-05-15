# 📘 Assignment: FastAPI CRUD with SQLite

## 🎯 Objective

Build a full CRUD REST API with FastAPI and SQLite to store, retrieve, update, and delete items persistently.

## 📝 Tasks

### 🛠️ Set Up FastAPI and SQLite

#### Description

Create the FastAPI application and initialize a SQLite database to store item data.

#### Requirements
Completed program should:

- Use `FastAPI()` to create the application.
- Initialize SQLite and create an `items` table if it does not exist.
- Define `GET /` to return a simple JSON welcome message.
- Include a `GET /items/` endpoint to return all stored items.

### 🛠️ Create and Read Items

#### Description

Add endpoints to create new items and retrieve individual items by ID.

#### Requirements
Completed program should:

- Define a Pydantic model for item data with `name`, `description`, `price`, and `in_stock` fields.
- Define `POST /items/` to add a new item to the database and return the stored item.
- Define `GET /items/{item_id}` to return the requested item or a 404 error when not found.

### 🛠️ Update and Delete Items

#### Description

Implement update and delete operations so the API supports the full CRUD lifecycle.

#### Requirements
Completed program should:

- Define `PUT /items/{item_id}` to update an existing item.
- Define `DELETE /items/{item_id}` to remove an item from the database.
- Return appropriate success responses and 404 errors for missing items.
