import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
reverse_number = importlib.import_module("Code.08_reverse_number").reverse_number

def test_positive_number():
    assert reverse_number(12345) == 54321
    assert reverse_number(1200) == 21

def test_negative_and_zero():
    assert reverse_number(-456) == -654
    assert reverse_number(0) == 0

if __name__ == "__main__":
    test_positive_number()
    test_negative_and_zero()
    print("All test cases passed.")
