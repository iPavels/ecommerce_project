import pytest

from src.Product import Product


def test_product_init():
    product = Product("Телефон", "Смартфон", 25000, 5)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 25000
    assert product.quantity == 5