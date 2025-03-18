import pytest

from src.Category import Category
from src.Lawn_Grass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone


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


@pytest.fixture
def smartphone_fix1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_fix2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                      98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_fix1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_fix2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")
