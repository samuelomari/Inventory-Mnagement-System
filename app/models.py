"""
Data model definitions for the inventory application.

This project uses an in-memory list of dictionaries instead of a database.
This helper function creates inventory items in a consistent format.
"""

def build_inventory_item(
    product_name,
    brands,
    stock,
    price,
    item_id=None,
    ingredients=None,
    nutriments=None,
):
    """Create and return an inventory item."""

    item = {
        "id": item_id if item_id is not None else 0,
        "product_name": product_name,
        "brands": brands,
        "stock": stock,
        "price": price,
    }

    # Add ingredients if they are provided
    if ingredients is not None:
        item["ingredients"] = ingredients

    # Add nutriments if they are provided
    if nutriments is not None:
        item["nutriments"] = nutriments

    return item
