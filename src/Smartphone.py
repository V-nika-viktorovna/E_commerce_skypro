from src.Product import Product


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Выводит полную стоимость всех товаров на складе"""

        if type(other) is Smartphone:
            return (self.quantity * self.__price) + (other.quantity * other.__price)
        else:
            raise TypeError
