import pytest

from src.Product import LawnGrass, Product, Smartphone


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


def test_product_str():
    p = Product("Телефон", "Смартфон", 80, 15)
    assert str(p) == "Телефон, 80 руб. Остаток: 15 шт."


def test_product_add():
    a = Product("Телефон", "Смартфон", 100, 10)
    b = Product("Ноутбук", "Игровой", 200, 2)
    result = a + b
    assert result == 1400  # 100*10 + 200*2


def test_product_add_type_error():
    a = Product("Телефон", "Смартфон", 100, 10)
    with pytest.raises(
        TypeError, match="Складывать можно только объекты класса Product"
    ):
        a + 10


def test_product_add_different_types():
    """Проверка, что нельзя складывать разные типы продуктов"""

    s = Smartphone("iPhone", "Телефон", 100000, 2, "A15", "Pro", 256, "черный")
    g = LawnGrass("Газон", "Трава", 500, 10, "Россия", 30, "зеленая")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        _ = s + g


def test_product_zero_quantity_raises_error():
    """Создание продукта с quantity=0 должно вызывать ValueError"""
    with pytest.raises(ValueError) as exc:
        Product("Test", "Desc", 100, 0)

    assert str(exc.value) == "Товар с нулевым количеством не может быть добавлен"
