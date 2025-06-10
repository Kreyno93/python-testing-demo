import pytest
from calc import add, subtract, multiply, divide
from calc import square_root, power, factorial


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
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    assert divide(0, 1) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by Zero"):
        divide(5, 0)


def test_square_root():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root(9) == 3
    assert square_root(2) == 2**0.5


def test_square_root_negative():
    with pytest.raises(
        ValueError, match="Cannot compute square root of negative number"
    ):
        square_root(-1)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25
    assert power(0, 5) == 0


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6


def test_factorial_negative():
    with pytest.raises(ValueError, match="Cannot compute factorial of negative number"):
        factorial(-3)
