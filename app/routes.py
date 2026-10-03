from flask import Flask, jsonify

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "stock": 10,
        "price": 3.99,
    }
]

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify({"status": 1, "inventory": inventory})

    @app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify({"status": 1, "inventory": inventory})

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = next((prod for prod in inventory if prod["id"] == item_id), None)
    if item is None:
        return jsonify({"status": 0, "message": "Item not found"}), 404
    return jsonify({"status": 1, "item": item})