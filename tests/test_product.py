import pytest

from src.Product import Product


def test_product_init_and_getter():
    p = Product("Телефон", "Смартфон", 25000, 5)
    assert p.name == "Телефон"
    assert p.price == 25000
    assert p.quantity == 5


def test_product_setter_positive():
    p = Product("Телефон", "Смартфон", 25000, 5)
    p.price = 30000
    assert p.price == 30000


def test_product_setter_negative(capsys):
    p = Product("Телефон", "Смартфон", 25000, 5)
    p.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 25000


def test_product_new_product():
    data = {"name": "Ноутбук", "description": "Игровой", "price": 80000, "quantity": 2}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Ноутбук"
    assert product.price == 80000
    assert product.quantity == 2


#  Новый тест для строкового представления продукта (__str__)
def test_product_str():
    p = Product("Телефон", "Смартфон", 80, 15)
    assert str(p) == "Телефон, 80 руб. Остаток: 15 шт."


# 🔹 Новый тест для корректной работа сложения двух продуктов (__add__)
def test_product_add():
    a = Product("Телефон", "Смартфон", 100, 10)
    b = Product("Ноутбук", "Игровой", 200, 2)
    result = a + b
    assert result == 1400  # 100*10 + 200*2


# 🔹 Новый тест проверки ошибки при сложении с неподдерживаемым типом
def test_product_add_type_error():
    a = Product("Телефон", "Смартфон", 100, 10)
    with pytest.raises(
        TypeError, match="Складывать можно только объекты класса Product"
    ):
        a + 10
