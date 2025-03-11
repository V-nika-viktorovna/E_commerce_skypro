class Product():
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}; {self.price} руб; Остаток: {self.quantity} шт.\n'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):

        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if new_price < self.__price:
                while True:
                    confirmation = input(f'\n\
    Вы действительно хотите установить цену ниже?\n\
    Если да, то введите "y", если нет, то введите "n"\n')
                    if confirmation == 'y':
                        self.__price = new_price
                        return self.__price
                        break
                    elif confirmation == 'n':
                        break
                    else:
                        print('Вы ввели неверное значение. Введите "y" либо "n"')
                        continue

    @classmethod
    def new_product(cls, params: dict, category=None):

        if category:

            list = category.products.split('\n')
            result = []
            for str_list in list:
                list_str = str_list.split('; ')
                if len(list_str) > 1:
                    dict_result = {
                        'name': list_str[0],
                        'price': list_str[1].split(' ')[0],
                        'quantity': list_str[2].split(' ')[1]
                    }
                    result.append(dict_result)
                else:
                    break

            for product in result:
                if params.get('name') == product.get('name'):
                    result_quantity = params.get('quantity') + int(product.get('quantity'))
                    if params.get('price') < float(product.get('price')):
                        result_price = product.get('price')
                        product['quantity'] = result_quantity
                        product['price'] = result_price

                    elif params.get('price') > float(product.get('price')):

                        result_price = params.get('price')
                        result_product = {
                            'name': product['name'],
                            'description': params['description'],
                            'price': result_price,
                            'quantity': result_quantity
                        }
            return cls(**result_product)
        return cls(**params)

    def __add__(self, other):
        """Выводит полную стоимость всех товаров на складе"""
        return (self.quantity * self.__price) + (other.quantity * other.__price)


if __name__ == '__main__':
    pr1 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 10)
    pr2 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 19000.0, 1)
    print(pr1+pr2)
