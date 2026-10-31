import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
word_frequency = importlib.import_module("Code.20_word_frequency").word_frequency

def test_word_frequency():
    assert word_frequency("hello world hello") == {"hello": 2, "world": 1}
    assert word_frequency("DevOps, devops! DEVOPS.") == {"devops": 3}
    assert word_frequency("") == {}

if __name__ == "__main__":
    test_word_frequency()
    print("All test cases passed.")
