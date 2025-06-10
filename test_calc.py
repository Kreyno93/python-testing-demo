import pytest
from calc import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-2, -2) == 0


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    assert divide(0, 1) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by Zero"):
        divide(5, 0)
