import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
second_largest = importlib.import_module("Code.15_second_largest").second_largest

def test_second_largest():
    assert second_largest([10, 20, 4, 45, 99]) == 45
    assert second_largest([10, 10, 9]) == 9
    assert second_largest([5, 5, 5]) is None
    assert second_largest([-1, -5, -3]) == -3

if __name__ == "__main__":
    test_second_largest()
    print("All test cases passed.")
