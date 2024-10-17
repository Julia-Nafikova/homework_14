import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(first_category.list_product) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_category_products_property(first_category):
    assert first_category.products == 'Samsung, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n'


def test_add_product():
    category_test = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=[]
    )
    product_test = Product(
        name='Nokia',
        description='212GB, blue цвет, 150MP камера',
        price=55000.0,
        quantity=1
    )

    category_test.add_product(product_test)

    assert category_test.product_count == 6


def test_category_str(first_category):
    assert str(first_category) == 'Смартфоны, количество продуктов: 13 шт.'


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung"
    assert next(category_iterator).name == 'Iphone 15'

    with pytest.raises(StopIteration):
        next(category_iterator)
