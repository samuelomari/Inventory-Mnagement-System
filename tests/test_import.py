from unittest.mock import patch

from app import app, inventory


@patch("app.external_api.fetch_product_by_barcode")
def test_import_external_product(mock_fetch):

    # Start with an empty inventory
    inventory.clear()

    product = {
        "code": "99999",
        "product_name": "Imported Almond Milk",
        "brands": "ImportBrand",
        "ingredients_text": "water, almonds",
        "nutriments": {
            "energy": 120
        },
    }

    # Fake the API response
    mock_fetch.return_value = product

    client = app.test_client()

    response = client.post("/inventory/import/99999")

    data = response.get_json()

    assert response.status_code == 201
    assert data["status"] == 1

    item = data["item"]

    assert item["product_name"] == "Imported Almond Milk"
    assert item["brands"] == "ImportBrand"
    assert item["ingredients"] == "water, almonds"
    assert item["nutriments"]["energy"] == 120
