import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
remove_duplicates = importlib.import_module("Code.16_remove_duplicates").remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    assert remove_duplicates([]) == []

if __name__ == "__main__":
    test_remove_duplicates()
    print("All test cases passed.")
