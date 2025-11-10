from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта"""
        pass
