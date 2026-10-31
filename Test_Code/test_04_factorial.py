import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
factorial = importlib.import_module("Code.04_factorial").factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(6) == 720

if __name__ == "__main__":
    test_factorial_zero()
    test_factorial_one()
    test_factorial_positive()
    print("All test cases passed.")
