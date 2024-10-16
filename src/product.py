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

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.price * other.quantity

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
            check_input = input("Изменять цену? Введите y если да,и n если нет.\n")
            if check_input != 'y':
                return
        self.__price = new_price


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)