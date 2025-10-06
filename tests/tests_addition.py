from app.calculator import Calculator

def test_addition():
   result = Calculator.addition(val1=2, val2= 2)
   assert result == 4, "The addition function returns the wrong value"
