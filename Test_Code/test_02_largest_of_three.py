import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
largest_of_three = importlib.import_module("Code.02_largest_of_three").largest_of_three

def test_largest_positive():
    assert largest_of_three(10, 25, 15) == 25

def test_largest_negative():
    assert largest_of_three(-10, -5, -20) == -5

def test_largest_equal():
    assert largest_of_three(7, 7, 7) == 7

if __name__ == "__main__":
    test_largest_positive()
    test_largest_negative()
    test_largest_equal()
    print("All test cases passed.")
