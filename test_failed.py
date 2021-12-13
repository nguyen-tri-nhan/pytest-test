import random
from pytest_check import check
from Calculator import Calculator


def test_failed():
    assert Calculator.add(3, 5) == 7


def test_failed_2():
    assert Calculator.add(3, 5) == 4


def test_failed_3():
    assert Calculator.add(3, 5) == 3


def test_failed_4():
    assert Calculator.add(3, 5) == 2


def test_failed_5():
    assert Calculator.add(3, 5) == 1


def test_failed_6():
    assert Calculator.add(3, 5) == 0


def test_failed_7():
    assert Calculator.add(3, 5) == -1


def test_failed_8():
    assert Calculator.add(3, 5) == -2


def test_failed_9():
    assert Calculator.add(3, 5) == 9

