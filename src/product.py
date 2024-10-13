from tabnanny import check


class Product:
    '''Класс для представления продукта'''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        '''Метод инициализации класса продукта. Задаем значения атрибутам'''
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product, products=None):
        if products:
            for product in products:
                if product.name == dict_product['name']:
                    product.quantity += dict_product['quantity']
                    product.price = max([product.price, dict_product['price']])
                    return product
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        if new_price < self.__price:
            check = input("Изменять цену y / n ")
            if check != 'y':
                return
        self.__price = new_price
