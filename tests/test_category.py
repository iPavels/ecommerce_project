import pytest

from src.Category import Category
from src.Product import Product


def test_category_init_and_counters():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Телефон", "Смартфон", 25000, 5)
    p2 = Product("Ноутбук", "Игровой ноутбук", 80000, 2)

    category = Category("Электроника", "Гаджеты", [p1, p2])

    assert category.name == "Электроника"
    assert category.description == "Гаджеты"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2