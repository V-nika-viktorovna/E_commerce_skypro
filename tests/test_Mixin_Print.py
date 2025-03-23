def test_Mixin_Print_Product(capsys, products_fix):
    result = capsys.readouterr()
    assert result.out.split('\n')[0] == 'Product(Fly GS Ultra, 256GB, Серый цвет, 200MP камера, 18000.0, 10)'


def test_Mixin_Print_LawnGrass(capsys, lawn_grass_fix1):
    result = capsys.readouterr()
    assert result.out.split('\n')[0] == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)'


def test_Mixin_Print_Smartphone(capsys, smartphone_fix1):
    result = capsys.readouterr()
    assert result.out.split('\n')[0] == 'Smartphone(Samsung Galaxy S23 Ultra, \
256GB, Серый цвет, 200MP камера, 180000.0, 5)'
