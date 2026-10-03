from cli import add_inventory_item, delete_inventory_item, list_inventory
from app import inventory


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


def test_list_inventory(capsys):

    reset_inventory()

    list_inventory()

    captured = capsys.readouterr()

    assert "Organic Almond Milk" in captured.out


def test_add_inventory_item():

    reset_inventory()

    item = add_inventory_item(
        "Test Product",
        "Test Brand",
        5,
        2.99
    )

    assert item["id"] == 2
    assert item["product_name"] == "Test Product"
    assert item["stock"] == 5
    assert item["price"] == 2.99


def test_delete_inventory_item():

    reset_inventory()

    item = add_inventory_item(
        "Delete Product",
        "Delete Brand",
        3,
        1.99
    )

    deleted_item = delete_inventory_item(item["id"])

    assert deleted_item is not None
    assert deleted_item["id"] == item["id"]
    assert deleted_item["product_name"] == "Delete Product"
