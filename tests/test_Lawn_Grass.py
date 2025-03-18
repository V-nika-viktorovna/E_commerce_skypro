import pytest


def test_Lawn_Grass_init(lawn_grass_fix1):
    assert lawn_grass_fix1.name == "Газонная трава"
    assert lawn_grass_fix1.description == "Элитная трава для газона"
    assert lawn_grass_fix1.quantity == 20
    assert lawn_grass_fix1.country == "Россия"
    assert lawn_grass_fix1.germination_period == "7 дней"
    assert lawn_grass_fix1.color == "Зеленый"


def test_Lawn_Grass_add(lawn_grass_fix1, lawn_grass_fix2):
    result = lawn_grass_fix1 + lawn_grass_fix2
    assert result == 16750.0


def test_Smartphone_add_error(lawn_grass_fix1):
    with pytest.raises(TypeError):
        lawn_grass_fix1 + 'jhgjhdgjdhg'
