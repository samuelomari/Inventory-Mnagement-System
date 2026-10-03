from flask import Flask, jsonify, request

from .models import build_inventory_item

app = Flask(__name__)

# In-memory inventory list
inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "ingredients": "Filtered water, almonds, cane sugar",
        "nutriments": {"energy": 50},
        "stock": 10,
        "price": 3.99,
    },
    {
        "id": 2,
        "product_name": "Whole Wheat Bread",
        "brands": "BakerCo",
        "ingredients": "Whole wheat flour, water, yeast, salt",
        "nutriments": {"energy": 250},
        "stock": 25,
        "price": 2.49,
    }
]


@app.route("/inventory", methods=["GET"])
def get_inventory():
    """Return all inventory items."""
    return jsonify({
        "status": 1,
        "inventory": inventory
    })


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    """Return one inventory item."""

    for item in inventory:
        if item["id"] == item_id:
            return jsonify({
                "status": 1,
                "item": item
            })

    return jsonify({
        "status": 0,
        "message": "Item not found"
    }), 404


@app.route("/inventory", methods=["POST"])
def add_inventory_item():

    data = request.get_json()

    if (
        "product_name" not in data or
        "brands" not in data or
        "stock" not in data or
        "price" not in data
    ):
        return jsonify({
            "status": 0,
            "message": "Invalid data"
        }), 400

    item_id = len(inventory) + 1

    new_item = build_inventory_item(
        product_name=data["product_name"],
        brands=data["brands"],
        stock=data["stock"],
        price=data["price"],
        item_id=item_id,
    )

    inventory.append(new_item)

    return jsonify({
        "status": 1,
        "item": new_item
    }), 201

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)

            return jsonify({
                "status": 1,
                "deleted": item
            })

    return jsonify({
        "status": 0,
        "message": "Item not found"
    }), 404


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):

    data = request.get_json()

    for item in inventory:

        if item["id"] == item_id:

            if "product_name" in data:
                item["product_name"] = data["product_name"]

            if "brands" in data:
                item["brands"] = data["brands"]

            if "stock" in data:
                item["stock"] = data["stock"]

            if "price" in data:
                item["price"] = data["price"]

            return jsonify({
                "status": 1,
                "item": item
            })

    return jsonify({
        "status": 0,
        "message": "Item not found"
    }), 404

@app.route("/inventory/find/<barcode>", methods=["GET"])
def find_external_product(barcode):

    from .external_api import fetch_product_by_barcode

    product = fetch_product_by_barcode(barcode)

    if product is None:
        return jsonify({
            "status": 0,
            "message": "Product not found"
        }), 404

    return jsonify({
        "status": 1,
        "product": product
    })


@app.route("/inventory/import/<barcode>", methods=["POST"])
def import_external_product(barcode):

    from .external_api import fetch_product_by_barcode

    product = fetch_product_by_barcode(barcode)

    if product is None:
        return jsonify({
            "status": 0,
            "message": "Product not found"
        }), 404

    item_id = len(inventory) + 1

    new_item = build_inventory_item(
        product_name=product.get("product_name", ""),
        brands=product.get("brands", ""),
        stock=0,
        price=0.0,
        item_id=item_id,
        ingredients=product.get("ingredients_text"),
        nutriments=product.get("nutriments"),
    )

    inventory.append(new_item)

    return jsonify({
        "status": 1,
        "item": new_item
    }), 201


@app.route("/inventory/find_name/<name>", methods=["GET"])
def find_products_by_name(name):

    from .external_api import fetch_products_by_name

    products = fetch_products_by_name(name)

    if not products:
        return jsonify({
            "status": 0,
            "message": "No products found"
        }), 404

    return jsonify({
        "status": 1,
        "products": products
    })


if __name__ == "__main__":
    app.run(debug=True)
