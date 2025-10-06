from app.calculator import multiply

def test_multiplication():
    result = multiply(val1=2, val2=2)
    assert result == 4

