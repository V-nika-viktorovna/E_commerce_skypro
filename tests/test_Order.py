from src.Order import Order


def test_Order_try(products_fix):
    result = Order(products_fix, 2)
    assert str(result) == 'Состав заказа: \nFly GS Ultra, 18000.0 руб. Остаток: 10 шт.\n в колличестве: 2шт.\
\nСтоимость заказа: 36000.0'


def test_Order_not_enough(products_fix):
    result = Order(products_fix, 20)
    assert str(result) == 'Нет необходимого количества товара!'
