""" TEST MULTIPLY """
from app.multiplication import multiply

def test_multiplication():
    """ MULTIPLY """
    result = multiply(10, 2)
    assert result == 20