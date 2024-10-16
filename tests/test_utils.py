from collections import namedtuple

import pytest

from src.category import Category
from src.product import Product
from src.utils import read_json, create_objects_from_json


def test_read_json(path, data):
    assert read_json(path) == [{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]}, {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 'products': [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]


# Data = namedtuple('Data', ['categories'])
# TestData = Data([{'products': ['product1', 'product2']}, {'products': ['product3']}])
#
# @pytest.mark.parametrize('data', [TestData])
# def test_create_objects_from_json(data):
#     # Ожидаемый результат
#     expected_result = [
#         Category('category1', 'category1', {'products': [Product('product1', 'product1', 'product1', 'product1'), Product('product2', 'product2', 'product2', 'product2')]}),
#         Category('category2', 'category2', {'products': [Product('product3', 'product3', 'product3', 'product3')]})
#     ]
#     # Вызов функции
#     result = create_objects_from_json(data)
#
#     # Проверка результата
#     assert result == expected_result