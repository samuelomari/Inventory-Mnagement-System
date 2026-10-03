from unittest.mock import patch, Mock

from app.external_api import fetch_product_by_barcode


def make_response(data, status_code=200):
    """Create a fake API response."""

    response = Mock()

    response.status_code = status_code
    response.json.return_value = data

    def raise_for_status():
        if status_code >= 400:
            raise Exception("HTTP Error")

    response.raise_for_status = raise_for_status

    return response


@patch("app.external_api.requests.get")
def test_fetch_product_success(mock_get):

    product = {
        "status": 1,
        "product": {
            "code": "12345",
            "product_name": "Mock Almond Milk",
            "brands": "MockBrand",
            "ingredients_text": "water, almonds",
            "nutriments": {
                "energy": 100
            },
        },
    }

    mock_get.return_value = make_response(product)

    result = fetch_product_by_barcode("12345")

    assert result is not None
    assert result["product_name"] == "Mock Almond Milk"
    assert result["brands"] == "MockBrand"


@patch("app.external_api.requests.get")
def test_fetch_product_not_found(mock_get):

    product = {
        "status": 0
    }

    mock_get.return_value = make_response(product)

    result = fetch_product_by_barcode("00000")

    assert result is None
