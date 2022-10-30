# project/app/tests/test_fibonacci.py

from app.algorithms.fibonacci import get_nth_fibo


def test_get_nth_fibo_with_negative_value():
    assert get_nth_fibo(-10) == "Please enter a positive integer"


def test_get_nth_fibo_with_zero():
    assert get_nth_fibo(0) == "Please enter a positive integer"


def test_get_nth_fibo_with_one():
    assert get_nth_fibo(1) == 1


def test_get_nth_fibo():
    assert get_nth_fibo(12) == 144
