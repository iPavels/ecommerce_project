class Product:
    """
    Класс для описания продукта
    """

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(
                f"Цена снижается с {self.__price} до {new_price}. Подтвердить? (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, data: dict, products: list = None):
        """
        Создаёт объект Product из словаря.
        Проверяет дубликаты по имени: увеличивает количество, цена = более высокая.
        """
        if products:
            for product in products:
                if product.name == data["name"]:
                    product.quantity += data["quantity"]
                    if data["price"] > product.price:
                        product.price = data["price"]
                    return product

        return cls(data["name"], data["description"], data["price"], data["quantity"])

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")

        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
