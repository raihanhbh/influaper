# project/tests/test_factorial.py

from app.algorithms.factorial import calc_factorial


def test_get_factorial_with_negative_value():
    assert calc_factorial(-1) == "Please enter a positive integer"


def test_get_factorial_with_zero():
    assert calc_factorial(0) == 1


def test_get_factorial():
    assert calc_factorial(3) == 6
