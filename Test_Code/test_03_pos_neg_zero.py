import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
check_pos_neg_zero = importlib.import_module("Code.03_pos_neg_zero").check_pos_neg_zero

def test_positive():
    assert check_pos_neg_zero(15) == "Positive"

def test_negative():
    assert check_pos_neg_zero(-8) == "Negative"

def test_zero():
    assert check_pos_neg_zero(0) == "Zero"

if __name__ == "__main__":
    test_positive()
    test_negative()
    test_zero()
    print("All test cases passed.")
