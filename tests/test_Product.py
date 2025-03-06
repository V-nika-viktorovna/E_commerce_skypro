def test_Product_try(products_fix):
    assert products_fix.name == "Fly GS Ultra"
    assert products_fix.description == "256GB, Серый цвет, 200MP камера"
    assert products_fix.price == 18000.0
    assert products_fix.quantity == 10
