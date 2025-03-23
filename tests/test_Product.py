import unittest.mock
from unittest.mock import patch

from src.Product import Product


def test_Product_try(products_fix):
    assert products_fix.name == "Fly GS Ultra"
    assert products_fix.description == "256GB, Серый цвет, 200MP камера"
    assert products_fix.price == 18000.0
    assert products_fix.quantity == 10


def test_Product_price_property_try(products_fix):
    assert products_fix.price == 18000.0


class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['y'])
    def test_Product_price_setter_try_yes(self, mock_input):
        new_product21 = Product.new_product(
            {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
             "quantity": 5})
        new_product21.price = 1800
        assert new_product21.price == 1800
        mock_input.assert_called()

    @patch('builtins.input', side_effect=['n'])
    def test_Product_price_setter_try_no(self, mock_input):
        new_product = Product.new_product(
            {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
             "quantity": 5})
        new_product.price = 800
        assert new_product.price == 180000.0
        mock_input.assert_called()


def test_Product_price_setter_try_zero(capsys):
    new_product = Product(
         name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0,
         quantity=5)
    new_product.price = -800
    captured = capsys.readouterr()
    assert captured.out.split('\n')[-2] == 'Цена не должна быть нулевая или отрицательная'
    assert new_product.price == 180000.0


def test_Product_new_product_classmethod_not_category():
    new_product1 = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product1.name == "Samsung Galaxy S23 Ultra"


def test_Product_new_product_classmethod_category(categoryes_fix):
    category_test = categoryes_fix
    new_product3 = Product.new_product(
        {"name": "Fly GS Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 190000.0,
         "quantity": 5}, category_test)
    print(new_product3)
    assert new_product3.name == "Fly GS Ultra"
    assert new_product3.quantity == 10


def test_Product_str(products_fix):
    assert str(products_fix) == 'Fly GS Ultra, 18000.0 руб. Остаток: 10 шт.\n'


def test_Product_add(products_fix):
    pr1 = Product("Lay Ultra", "512GB, Серый цвет, 200MP камера", 20000.0, 5)
    assert (products_fix+pr1) == 280000.0
