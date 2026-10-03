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