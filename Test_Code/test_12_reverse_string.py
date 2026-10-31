import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
reverse_string = importlib.import_module("Code.12_reverse_string").reverse_string

def test_reverse_string():
    assert reverse_string("DevOps") == "spOveD"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""

if __name__ == "__main__":
    test_reverse_string()
    print("All test cases passed.")
