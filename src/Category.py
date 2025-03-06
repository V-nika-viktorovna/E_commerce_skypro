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

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}; {product.price} руб; Остаток: {product.quantity} шт.\n'

        return products_str

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    print(category1.product_count)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

    a_test = Product(name='aaaa', description='kjhgmjhgj', price=12, quantity=1)
    c_test = Product(name='abbbb', description='kjhgmjhgjm', price=11, quantity=3)
    category11 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [a_test, c_test]
    )

    b_test = Product.new_product({'name': 'abbbb', 'description': 'kjhgmjhgjm', 'price': 15,
                                  'quantity': 2}, category=category11)

    print(b_test.price)
    print(b_test.quantity)
