import os.path
from unittest.mock import patch

from src.utils import get_data_object_class


@patch('json.load')
def test_get_data_object_class_try(mock_get):
    mock_get.return_value = [{'name': 'Смартфончики :)))',
                             'description': 'Смартфоны, как средство не только коммуникации, \
                             но и получение дополнительных функций для удобства жизни',
                             'products': [
                                 {'name': 'Samsung Galaxy C23 Ultra',
                                  'description': '256GB, Серый цвет, 200MP камера',
                                  'price': 180000.0, 'quantity': 5},
                                 {'name': 'Iphone 15',
                                  'description': '512GB, Gray space',
                                  'price': 210000.0, 'quantity': 8},
                                 {'name': 'Xiaomi Redmi Note 11',
                                  'description': '1024GB, Синий',
                                  'price': 31000.0, 'quantity': 14}]},
                            {'name': 'Телевизоры - обзоры',
                             'description': 'Современный телевизор, который позволяет наслаждаться просмотром, \
                             станет вашим другом и помощником',
                             'products': [
                                 {'name': '55" QLED 4K',
                                  'description': 'Фоновая подсветка',
                                  'price': 123000.0,
                                  'quantity': 7}]}
                            ]
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    FILE_DIR = os.path.join(DATA_DIR, 'products_test.json')
    result = get_data_object_class(FILE_DIR)
    assert result[0].name == 'Смартфончики :)))'
    assert result[1].name == 'Телевизоры - обзоры'


def test_get_data_object_class_none():
    assert get_data_object_class("") == []
