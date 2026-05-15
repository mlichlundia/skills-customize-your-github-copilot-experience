# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework to define endpoints, validate request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Setup FastAPI Application

#### Description

Create a FastAPI app with a root endpoint and a collection of items. This task introduces routing and response formatting.

#### Requirements
Completed program should:

- Use `FastAPI()` to create an application instance.
- Define `GET /` to return a welcome JSON message.
- Define `GET /items/` to return a list of items.
- Define `GET /items/{item_id}` to return a specific item or a 404 error when the item is missing.

### 🛠️ Add Data Validation and Create Item Endpoint

#### Description

Use a Pydantic model to validate incoming JSON and add an endpoint that creates new items.

#### Requirements
Completed program should:

- Define a Pydantic `Item` model with fields for `name`, `description`, `price`, and `in_stock`.
- Define `POST /items/` to accept JSON data and return the created item.
- Validate request data automatically using FastAPI and Pydantic.
- Return a JSON response containing the new item ID and item data.
