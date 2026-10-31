import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
check_even_odd = importlib.import_module("Code.01_even_odd").check_even_odd

def test_even_number():
    assert check_even_odd(10) == "Even"

def test_odd_number():
    assert check_even_odd(7) == "Odd"

def test_zero():
    assert check_even_odd(0) == "Even"

def test_negative_even():
    assert check_even_odd(-4) == "Even"

def test_negative_odd():
    assert check_even_odd(-5) == "Odd"

if __name__ == "__main__":
    test_even_number()
    test_odd_number()
    test_zero()
    test_negative_even()
    test_negative_odd()
    print("All test cases passed.")
