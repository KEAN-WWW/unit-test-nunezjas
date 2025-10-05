import pytest
from app.calculator import Calculator

def test_division():
    assert Calculator.division(10, 2) == 5

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        Calculator.division(10, 0)