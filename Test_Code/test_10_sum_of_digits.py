import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sum_of_digits = importlib.import_module("Code.10_sum_of_digits").sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(1234) == 10
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-905) == 14

if __name__ == "__main__":
    test_sum_of_digits()
    print("All test cases passed.")
