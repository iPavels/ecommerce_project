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
        """Геттер: возвращает строку со всеми продуктами"""
        return "\n".join(str(product) for product in self.__products)

    @classmethod
    def new_product(cls, data: dict) -> Product:
        """Создает новый объект Product из словаря"""
        return Product.new_product(data)
