import requests


def fetch_product_by_barcode(barcode: str):
    """Fetch product details from OpenFoodFacts by barcode.

    Returns a simplified dict with selected fields or None if not found/error.
    """
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != 1:
            return None
        product = data.get("product", {})
        return {
            "code": product.get("code"),
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "ingredients_text": product.get("ingredients_text"),
            "nutriments": product.get("nutriments", {}),
        }
    except Exception:
        return None


def fetch_products_by_name(name: str, page_size: int = 5):
    """Search OpenFoodFacts for products matching `name`.

    Returns a list of simplified product dicts (max `page_size`).
    """
    url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": page_size,
    }
    try:
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        products = data.get("products", [])
        results = []
        for p in products[:page_size]:
            results.append({
                "code": p.get("code"),
                "product_name": p.get("product_name"),
                "brands": p.get("brands"),
                "ingredients_text": p.get("ingredients_text"),
            })
        return results
    except Exception:
        return []
