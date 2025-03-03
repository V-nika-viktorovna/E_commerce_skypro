def test_Category_try(categoryes_fix):
    assert categoryes_fix.name == "Смартфоны"
    assert categoryes_fix.description == "Смартфоны, как средство коммуникации"
    assert categoryes_fix.products == ["Fly GS Ultra", "Iphone 15"]
