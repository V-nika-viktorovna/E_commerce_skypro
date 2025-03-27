from src.Category import Category
from src.My_Exceptions import MyExceptions
from src.Product import Product


class Order(Category):

    product: Product
    quantity: int

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self):
        if self.quantity > self.product.quantity:
            return 'Нет необходимого количества товара!'
        else:
            return (f'Состав заказа: \n{self.product} в колличестве: {self.quantity}шт.\
\nСтоимость заказа: {self.total_price}')


if __name__ == '__main__':

    pr1 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 10)
    test = Order(pr1)

    print(str(test))

    try:
        pr2 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 11)
        pr3 = Product("Fly Ultra", "512GB, Серый цвет, 200MP камера", 20000.0, 0)
    except MyExceptions as e:
        print(str(e))
    else:
        print('Товар добавлен успешно')
    finally:
        print("Обработка добавления товара завершена. \n")

    try:
        pr2 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 11)
    except MyExceptions as e:
        print(str(e))
    else:
        print('Товар добавлен успешно')
    finally:
        print("Обработка добавления товара завершена.")
