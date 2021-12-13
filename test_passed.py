import random
from pytest_check import check
from Calculator import Calculator


def test_passed():
    assert Calculator.add(3, 5) == 8


