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
    product = Product('1', '2', 3.0, 4)
    product.name = '1'
    product.description = '2'
    product.price = 180000.0
    product.quantity = 5
