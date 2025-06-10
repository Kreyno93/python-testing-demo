import pytest
import calc


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-2, -2) == 0


def test_multiply():
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0


def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2
    assert calc.divide(0, 1) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by Zero"):
        calc.divide(5, 0)
