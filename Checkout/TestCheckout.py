import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    co = Checkout()
    co.addPrice("a", 10)
    co.addPrice("b", 20)
    return co

def test_calculate_total(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 10

def test_calculate_total_multiple_items(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 30

def test_can_add_discount(checkout):
    checkout.addDiscount("a",3,20)

def test_can_add_discountRules(checkout):
    checkout.addDiscount("a",3,20)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    print(checkout.calculateTotal())
    assert checkout.calculateTotal() == 20