import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def products_fix():
    return Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 10)


@pytest.fixture
def categoryes_fix():
    product1 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Смартфоны",
                    "Смартфоны, как средство коммуникации",
                    [product1, product2])
