import pytest
from src.shopping_cart import Product, ShoppingCart



@pytest.fixture
def sample_product1():
    return Product(78, "Tea", 14.5)

@pytest.fixture
def sample_product2():
    return Product(233, "Coffee", 23.4)

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def filled_cart(empty_cart, sample_product1, sample_product2):
    empty_cart.add_product(sample_product2, 5)
    empty_cart.add_product(sample_product1, 2)
    return empty_cart

def test_adding_positive(empty_cart, sample_product1):
    empty_cart.add_product(sample_product1)
    assert empty_cart.get_product_count() == 1
    assert empty_cart.get_total_price() == 14.5
    assert sample_product1.id in empty_cart.products.keys()

@pytest.mark.parametrize("quantity", [1, 5, 10])
def test_multiple_adding(empty_cart, sample_product2, quantity):
    empty_cart.add_product(sample_product2, quantity)
    assert empty_cart.get_product_count() == quantity

def test_removing_positive(filled_cart, sample_product2):
    filled_cart.remove_product(sample_product2.id)
    assert filled_cart.get_product_count() == 6
    assert filled_cart.products[sample_product2.id]["quantity"] == 4

def test_clear_cart(filled_cart, sample_product1, sample_product2):
    filled_cart.remove_product(sample_product1.id, 2)
    filled_cart.remove_product(sample_product2.id, 5)
    assert filled_cart.get_product_count() == 0
    assert sample_product1.id not in filled_cart.products.keys()
