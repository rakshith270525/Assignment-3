import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
find_missing_number = importlib.import_module("Code.18_missing_number").find_missing_number

def test_missing_number():
    assert find_missing_number([1, 2, 4, 5, 6]) == 3
    assert find_missing_number([2, 3, 4, 5]) == 1
    assert find_missing_number([1, 2, 3, 4]) == 5

if __name__ == "__main__":
    test_missing_number()
    print("All test cases passed.")
