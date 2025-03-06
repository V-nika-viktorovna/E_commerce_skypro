import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def products_fix():
    return Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 10)


@pytest.fixture
def categoryes_fix():
    return Category("Смартфоны",
                    "Смартфоны, как средство коммуникации",
                    ["Fly GS Ultra", "Iphone 15"])
