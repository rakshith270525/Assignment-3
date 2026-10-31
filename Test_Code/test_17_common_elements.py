import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
common_elements = importlib.import_module("Code.17_common_elements").common_elements

def test_common_elements():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert common_elements([1, 2], [3, 4]) == []
    assert common_elements([1, 1, 2], [1, 2, 2]) == [1, 2]

if __name__ == "__main__":
    test_common_elements()
    print("All test cases passed.")
