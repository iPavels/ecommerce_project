from src.Product import Product


class Category:
    """
    Класс для описания категории товаров.

    """

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products: [Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех товаров."""
        return "\n".join(str(product) for product in self.__products)

    @classmethod
    def new_product(cls, data: dict) -> Product:
        """Создает новый объект Product из словаря"""
        return Product.new_product(data)

    def get_average_price(self):
        """Возвращает среднюю цену товаров в категории"""
        try:
            total = sum(product.price for product in self.__products)
            count = len(self.__products)
            return total / count
        except ZeroDivisionError:
            return 0

    def __str__(self) -> str:
        """Строковое отображение категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
