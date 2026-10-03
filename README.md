# Inventory Management System

A small Flask-based inventory API with a beginner-friendly CLI.

## Setup

1. Create or activate the virtual environment:
   - Windows: `python -m venv .venv`
   - Activate: `.\.venv\Scripts\activate`
2. Install dependencies:
   - `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

## Run the API

Start the Flask app:

```bash
.\.venv\Scripts\python.exe app\routes.py
```

Then open `http://127.0.0.1:5000/inventory` in your browser or use Postman.

## API Endpoints

- `GET /inventory` - list all items
- `GET /inventory/<id>` - get one item by ID
- `POST /inventory` - add an item with JSON data
- `PATCH /inventory/<id>` - update an item by ID
- `DELETE /inventory/<id>` - delete an item by ID
 - `GET /inventory/find/<barcode>` - query external API (OpenFoodFacts) for barcode
    - Response: `{status:1, product: {code, product_name, brands, ingredients_text, nutriments}}`
 - `GET /inventory/find_name/<name>` - search external API for products by name
    - Response: `{status:1, products: [{code, product_name, brands, ingredients_text}]}`
 - `POST /inventory/import/<barcode>` - fetch external product and import into local inventory
    - Response: `201 Created` with `{status:1, item: <imported item>}`

## CLI Usage

List inventory:

```bash
python cli.py list
```

Add an item:

```bash
python cli.py add "Organic Almond Milk" Silk 10 3.99
```

Delete an item:

```bash
python cli.py delete 1
```

CLI API mode (call the running Flask API):

```bash
python cli.py api list
python cli.py api find 0123456789012
python cli.py api find_name "almond milk"
python cli.py api import 0123456789012
```

## What's implemented (grading alignment)

- Flask routing: GET/POST/PATCH/DELETE for `/inventory`, plus helper routes:
   - `GET /inventory/find/<barcode>` (external API lookup)
   - `GET /inventory/find_name/<name>` (external search)
   - `POST /inventory/import/<barcode>` (import external product)
- CRUD: full Create/Read/Update/Delete implemented and tested.
- External API: integrated with OpenFoodFacts via `app/external_api.py` (live calls at runtime; mocked in tests).
- CLI: beginner-friendly local commands and an `api` mode to call the running Flask app.
- Tests: pytest tests cover API endpoints, CLI helpers, and external API interactions (mocked). Run `pytest` to verify.

## How to run tests

Activate the virtualenv and run:

```bash
.\.venv\Scripts\activate
.\.venv\Scripts\python.exe -m pytest -q
```

## Notes

- The app uses an in-memory `inventory` list (no DB). Imported products store selected OpenFoodFacts fields.
- Tests mock external HTTP calls so they won't hit the network.
- Remaining optional task: build an admin UI (not included).

## Ready to push

I removed the original `Readme` file to avoid duplication. The repo is ready; run a final `git push` when you're ready to publish.
