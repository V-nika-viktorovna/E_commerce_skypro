import pytest


def test_Smartphone_init(smartphone_fix1):
    assert smartphone_fix1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_fix1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_fix1.quantity == 5
    assert smartphone_fix1.efficiency == 95.5
    assert smartphone_fix1.model == "S23 Ultra"
    assert smartphone_fix1.memory == 256
    assert smartphone_fix1.color == "Серый"


def test_Smartphone_add(smartphone_fix1, smartphone_fix2):
    result = smartphone_fix1 + smartphone_fix2
    assert result == 2580000.0


def test_Smartphone_add_error(smartphone_fix1):
    with pytest.raises(TypeError):
        smartphone_fix1 + 'jhgjhdgjdhg'
