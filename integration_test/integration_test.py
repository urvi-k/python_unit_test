# import addition
# import multiplication
from unittest import TestCase

import calculator


def test_integration():
    # Test multiplying the result of adding two numbers with another number
    assert calculator.multiply(calculator.add(2, 3), 4) == 20


## Unit testing

def test_addition():
    assert calculator.add(2, 3) == 5


def test_subtraction():
    assert calculator.subtract(5, 3) == 2

    def test_multiplication():
        assert calculator.multiply(2, 3) == 6

    def test_division():
        assert calculator.divide(6, 3) == 2

    def test_divide_by_zero():
        try:
            calculator.divide(6, 0)
        except ValueError as e:
            assert str(e) == "Cannot divide by zero"
        else:
            assert False, "Expected ValueError"


class Test(TestCase):
    def test_add(self):
        assert calculator.add(2, 3) == 5

    def test_subtract(self):
        assert calculator.subtract(5, 3) == 2

    def test_multiply(self):
        assert calculator.multiply(2, 3) == 6

    def test_divide(self):
        assert calculator.divide(6, 3) == 2
