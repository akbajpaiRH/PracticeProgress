import pytest

from Checkout import Checkout


@pytest.fixture()
def checkout():
    co = Checkout()
    return co


def test_add_item_price(checkout):
    checkout.addPrice("a", 10)


def test_can_add_item(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
