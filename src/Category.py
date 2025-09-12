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
        self.__products: list[products] = []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию и увеличивает счетчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми продуктами в категории."""
        return "\n".join(str(product) for product in self.__products)

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Создает новый объект Product из словаря."""
        return Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
