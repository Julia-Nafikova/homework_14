import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name='Samsung',
        description='256GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name='Iphone 15',
        description='512GB, Gray space',
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[
            Product('Samsung', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
            Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product("QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def new_price():
    return -1000


@pytest.fixture
def product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def path():
    raw_data = './data/products.json'
    return raw_data


@pytest.fixture
def data():
    data_json = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]
    return data_json


@pytest.fixture
def category_iterator(first_category):
    return CategoryIterator(first_category)
