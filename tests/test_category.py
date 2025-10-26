import pytest

from src.Category import Category
from src.Product import Product


def test_category_init_and_counters():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Телефон", "Смартфон", 25000, 5)
    p2 = Product("Ноутбук", "Игровой ноутбук", 80000, 2)

    c = Category("Электроника", "Гаджеты", [p1, p2])

    assert c.name == "Электроника"
    assert c.description == "Гаджеты"
    assert "Телефон" in c.products
    assert "Ноутбук" in c.products
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product():
    Category.product_count = 0
    c = Category("Техника", "Разное", [])
    p = Product("Миксер", "Кухонный", 5000, 7)

    c.add_product(p)

    assert "Миксер" in c.products
    assert Category.product_count == 1


def test_category_products_getter_format():
    p1 = Product("Холодильник", "LG", 45000, 4)
    c = Category("Бытовая техника", "Крупная", [p1])

    products_str = c.products
    assert "Холодильник, 45000 руб. Остаток: 4 шт." in products_str


def test_category_new_product():
    data = {"name": "Планшет", "description": "Android", "price": 30000, "quantity": 6}
    product = Category.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Планшет"
    assert product.price == 30000
    assert product.quantity == 6


def test_category_str():
    p1 = Product("Телефон", "Смартфон", 25000, 5)
    p2 = Product("Ноутбук", "Игровой", 80000, 3)
    c = Category("Электроника", "Гаджеты", [p1, p2])

    result = str(c)
    assert result == "Электроника, количество продуктов: 8 шт."


def test_category_add_product_type_error():
    c = Category("Одежда", "Мужская", [])
    with pytest.raises(
        TypeError, match="Можно добавлять только объекты класса Product"
    ):
        c.add_product("не продукт")
