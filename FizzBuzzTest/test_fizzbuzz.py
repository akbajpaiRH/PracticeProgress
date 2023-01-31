import pytest
from fizzbuzz import fizzbuzz
@pytest.mark.parametrize("test_input, expected_output",
[(1, 1),(2, 2),(3, "Fizz"),(5,"Buzz"),(15,"FizzBuzz"),(6,"Fizz")])
def test_fizzbuzz(test_input, expected_output):
    ret=fizzbuzz(test_input)
    assert ret == expected_output


# test_fizzbuzz(1, 1)
# test_fizzbuzz(2, 2)
# test_fizzbuzz(3, "Fizz")
# test_fizzbuzz(5, "Buzz")
# test_fizzbuzz(6, "Fizz")
# test_fizzbuzz(10, "Buzz")
# test_fizzbuzz(15, "FizzBuzz")
