from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category:
    '''Класс для представления категории'''
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        '''Метод инициализации класса категории. Задаем значения атрибутам'''
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        products_in_stock = 0
        for product in self.__products:
            products_in_stock += product.quantity
        return f'{self.name}, количество продуктов: {products_in_stock} шт.'

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Нельзя добавлять товар с нулевым количеством")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str

    @property
    def list_product(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
