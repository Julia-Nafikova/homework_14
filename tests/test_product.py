
def test_product_init(first_product):
    assert first_product.name == 'Samsung'
    assert first_product.description == '256GB, Серый цвет, 200MP камера'
    assert first_product.price == 180000.0
    assert first_product.quantity == 5