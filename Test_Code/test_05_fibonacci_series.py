import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
fibonacci_series = importlib.import_module("Code.05_fibonacci_series").fibonacci_series

def test_fibonacci_zero():
    assert fibonacci_series(0) == []

def test_fibonacci_one():
    assert fibonacci_series(1) == [0]

def test_fibonacci_multiple():
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]

if __name__ == "__main__":
    test_fibonacci_zero()
    test_fibonacci_one()
    test_fibonacci_multiple()
    print("All test cases passed.")
