import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
find_duplicates = importlib.import_module("Code.19_find_duplicates").find_duplicates

def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 5, 1]) == [2, 1]
    assert find_duplicates([1, 2, 3]) == []
    assert find_duplicates([5, 5, 5, 5]) == [5]

if __name__ == "__main__":
    test_find_duplicates()
    print("All test cases passed.")
