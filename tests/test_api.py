import pytest

from app import app, inventory


def reset_inventory():
    inventory.clear()

    inventory.append({
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "ingredients": "Filtered water, almonds, cane sugar",
        "nutriments": {"energy": 50},
        "stock": 10,
        "price": 3.99,
    })


def test_get_inventory():

    reset_inventory()

    client = app.test_client()

    response = client.get("/inventory")

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == 1
    assert isinstance(data["inventory"], list)

    # Check that item with ID 1 exists
    found = False

    for item in data["inventory"]:
        if item["id"] == 1:
            found = True

    assert found == True


def test_delete_inventory_item():

    reset_inventory()

    client = app.test_client()

    response = client.delete("/inventory/1")

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == 1
    assert data["deleted"]["id"] == 1


def test_create_inventory_item():

    reset_inventory()

    client = app.test_client()

    new_item = {
        "product_name": "New Product",
        "brands": "NewBrand",
        "stock": 5,
        "price": 1.99,
    }

    response = client.post("/inventory", json=new_item)

    data = response.get_json()

    assert response.status_code == 201
    assert data["status"] == 1
    assert data["item"]["product_name"] == "New Product"


def test_update_inventory_item():

    reset_inventory()

    client = app.test_client()

    updated_item = {
        "stock": 20,
        "price": 4.49
    }

    response = client.patch("/inventory/1", json=updated_item)

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == 1
    assert data["item"]["stock"] == 20
    assert data["item"]["price"] == 4.49
