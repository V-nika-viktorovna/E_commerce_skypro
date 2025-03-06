from src.Category import Category
from src.Product import Product


def test_Category_try(categoryes_fix):
    assert categoryes_fix.name == "Смартфоны"
    assert categoryes_fix.description == "Смартфоны, как средство коммуникации"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_Category_products_property_try(categoryes_fix):
    assert categoryes_fix.products == "Fly GS Ultra; 180000.0 руб; Остаток: 5 шт.\
\nIphone 15; 210000.0 руб; Остаток: 8 шт.\n"


def test_add_product_try(categoryes_fix, products_fix):
    categoryes_fix.add_product(product=Product("55\" QLED", "1024GB, Синий",
                                               12300.0, 7))
    assert categoryes_fix.products == 'Fly GS Ultra; 180000.0 руб; Остаток: 5 шт.\
\nIphone 15; 210000.0 руб; Остаток: 8 шт.\n\
55" QLED; 12300.0 руб; Остаток: 7 шт.\n'
