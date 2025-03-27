import pytest

from src.Category import Category
from src.iter_Category import IterCategory
from src.Product import Product


def test_Category_try(categoryes_fix):
    assert categoryes_fix.name == "Смартфоны"
    assert categoryes_fix.description == "Смартфоны, как средство коммуникации"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_Category_products_property_try(categoryes_fix):
    assert categoryes_fix.products == "Fly GS Ultra, 180000.0 руб. Остаток: 5 шт.\
\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_add_product_try(categoryes_fix, products_fix):
    categoryes_fix.add_product(product=Product("55\" QLED", "1024GB, Синий",
                                               12300.0, 7))
    assert categoryes_fix.products == 'Fly GS Ultra, 180000.0 руб. Остаток: 5 шт.\
\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n\
55" QLED, 12300.0 руб. Остаток: 7 шт.\n'


def test_Category_str(categoryes_fix):
    assert str(categoryes_fix) == 'Смартфоны, количество продуктов: 13 шт.'


def test_IterCategory_try(categoryes_fix):
    iter1 = IterCategory(categoryes_fix)

    assert next(iter1) == 'Fly GS Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert next(iter1) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'

    with pytest.raises(StopIteration):
        next(iter1)


def test_add_product_try_error(categoryes_fix):
    with pytest.raises(TypeError):
        categoryes_fix.add_product("jhgjhhghgh")


def test_Category_middle_price_try(categoryes_fix):
    assert categoryes_fix.middle_price() == 30000


# def test_Category_middle_price_zero(categoryes_fix):
#     product1 = Product("Iphone 16", "512GB, Gray space", 230000.0, 1)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
#     Category("Смартфоны", "Смартфоны, как средство коммуникации",
#              [product1, product2])
#     assert categoryes_fix.middle_price() == 0

def test_Category_middle_price_zero():
    result = Category("Пустая категория", "Категория без продуктов", [])
    assert result.middle_price() == 0
