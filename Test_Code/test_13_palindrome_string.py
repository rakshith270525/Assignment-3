import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
is_palindrome_string = importlib.import_module("Code.13_palindrome_string").is_palindrome_string

def test_palindrome_string():
    assert is_palindrome_string("madam") is True
    assert is_palindrome_string("Racecar") is True
    assert is_palindrome_string("hello") is False
    assert is_palindrome_string("") is True

if __name__ == "__main__":
    test_palindrome_string()
    print("All test cases passed.")
