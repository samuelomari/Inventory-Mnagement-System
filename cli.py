import sys

from app import inventory
from app.models import build_inventory_item


def list_inventory():
    """Display all inventory items."""
    for item in inventory:
        print(
            f"{item['id']}: {item['product_name']} ({item['brands']}) "
            f"- Stock: {item['stock']}, Price: ${item['price']}"
        )


def add_inventory_item(product_name, brands, stock, price):
    """Add a new item to the inventory."""

    item_id = len(inventory) + 1

    new_item = build_inventory_item(
        product_name,
        brands,
        stock,
        price,
        item_id
    )

    inventory.append(new_item)

    print("Item added successfully!")
    return new_item


def delete_inventory_item(item_id):
    """Delete an item using its ID."""

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            print("Item deleted successfully!")
            return item

    print("Item not found.")
    return None


def print_usage():
    print("Usage:")
    print("python cli.py list")
    print("python cli.py add <product_name> <brand> <stock> <price>")
    print("python cli.py delete <id>")


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print_usage()
        return

    command = args[0]

    if command == "list":
        list_inventory()

    elif command == "add":

        if len(args) != 5:
            print("Please provide all details.")
            return

        product_name = args[1]
        brands = args[2]
        stock = int(args[3])
        price = float(args[4])

        add_inventory_item(product_name, brands, stock, price)

    elif command == "delete":

        if len(args) != 2:
            print("Please provide an item ID.")
            return

        item_id = int(args[1])

        delete_inventory_item(item_id)

    else:
        print("Invalid command.")
        print_usage()


if __name__ == "__main__":
    main()
