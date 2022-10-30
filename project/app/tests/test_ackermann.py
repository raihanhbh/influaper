# project/tests/test_ackermann.py

from app.algorithms.ackermann import calc_ackermann


def test_calc_ackermann_with_m_zero():
    assert calc_ackermann(0, 4) == 5


def test_calc_ackermann_with_n_zero():
    assert calc_ackermann(2, 0) == 3


def test_calc_ackermann():
    assert calc_ackermann(1, 2) == 4
