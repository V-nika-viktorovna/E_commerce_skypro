import json
import os.path

from src.Category import Category
from src.Product import Product


def get_data_object_class(file_dir: str) -> list:
    """Функция принимает путь до файла json, считывает данные из json файла
    и создает объекты классов."""

    products_list = []
    categoryes_list = []

    try:
        with open(file_dir, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            print(data)
    except Exception:
        categoryes_list = []

    else:
        for category in data:
            for product in category.get('products'):
                products_list.append(Product(**product))

            try:
                category['products'] = products_list
                categoryes_list.append(Category(**category))
            except Exception:
                categoryes_list = []

    return categoryes_list


if __name__ == '__main__':
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CURRENT_DIR, '..', 'data')
    FILE_DIR = os.path.join(DATA_DIR, 'products.json')

    categoryes = get_data_object_class(FILE_DIR)

    print(categoryes[0].name)
    print(categoryes[1].name)
    print(categoryes[0].products[0].name)
    print(categoryes[1].products[3].name)
