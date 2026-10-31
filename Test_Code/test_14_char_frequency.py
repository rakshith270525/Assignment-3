import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
char_frequency = importlib.import_module("Code.14_char_frequency").char_frequency

def test_char_frequency():
    assert char_frequency("banana") == {"b": 1, "a": 3, "n": 2}
    assert char_frequency("") == {}
    assert char_frequency("aa") == {"a": 2}

if __name__ == "__main__":
    test_char_frequency()
    print("All test cases passed.")
