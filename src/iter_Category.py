from src.Category import Category
from src.Product import Product


class IterCategory():

    def __init__(self, category_obj: Category):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):

        stop_iter = len(self.category.products.split('\n')) - 1
        if self.index < stop_iter:
            product = self.category.products.split('\n')[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == '__main__':
    pr1 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 10)
    pr2 = Product("Fly GS Ultra", "256GB, Серый цвет, 200MP камера", 19000.0, 1)
    pr3 = Product("NJHJHJHJH 54544", "черный цвет, 120MP камера", 5000.0, 12)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [pr1, pr2, pr3])

    iter1 = IterCategory(category1)

    for prod in iter1:
        print(prod)
