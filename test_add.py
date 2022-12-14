import pytest
from main import add


def test_add():
    assert add(7, 3) == 10
    assert add("hello", "world") == "helloworld"
    assert add(10.5,2.5) == 13
