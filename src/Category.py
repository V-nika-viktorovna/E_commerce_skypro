from src.Base_Category import BaseCategory
from src.My_Exceptions import MyExceptions
from src.Product import Product


class Category(BaseCategory):
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        sum_quantity = 0
        for product in self.__products:
            sum_quantity += product.quantity
        return f'{self.name}, количество продуктов: {sum_quantity} шт.'

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += str(product)

        return products_str

    def add_product(self, product):

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
            print('Товар успешно добавлен')
        else:
            raise TypeError

    def middle_price(self) -> float:
        '''Метод, который подсчитывает средний ценник всех товаров'''

        cost_products = 0
        quantity_products = 0

        for product in self.__products:
            cost_products += product.price
            quantity_products += product.quantity

        try:
            middle_price = cost_products/quantity_products
        except ZeroDivisionError:
            return 0
        else:
            return round(middle_price, 2)


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except MyExceptions:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт"
            " с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
