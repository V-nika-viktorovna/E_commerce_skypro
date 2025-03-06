from src.Category import Category


def test_Category_try(categoryes_fix):
    assert categoryes_fix.name == "Смартфоны"
    assert categoryes_fix.description == "Смартфоны, как средство коммуникации"
    assert categoryes_fix.products == ["Fly GS Ultra", "Iphone 15"]
    assert Category.category_count == 1
    assert Category.product_count == 2
