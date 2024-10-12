

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
    def new_product(cls, dict_product):
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def prise(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price