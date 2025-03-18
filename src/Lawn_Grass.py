from src.Product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Выводит полную стоимость всех товаров на складе"""

        if type(other) is LawnGrass:
            return (self.quantity * self.__price) + (other.quantity * other.__price)

        else:
            raise TypeError
