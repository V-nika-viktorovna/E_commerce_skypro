from src.Product import Product


class Category():
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

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":

    if __name__ == '__main__':
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        print(str(product1))
        print(str(product2))
        print(str(product3))

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3]
        )

        print(str(category1))

        print(category1.products)

        print(product1 + product2)
        print(product1 + product3)
        print(product2 + product3)
