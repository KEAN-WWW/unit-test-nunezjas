import pytest
from app.calculator import Calculator

def test_addition():
    assert Calculator.addition(1, 1) == 2


def test_subtraction():
    assert Calculator.subtraction(10, 5) == 5

def test_multiplication():
    assert Calculator.multiplication(4, 2) == 8


def test_division():
    assert Calculator.division(10, 2) == 5
