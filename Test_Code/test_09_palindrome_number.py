import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
is_palindrome_number = importlib.import_module("Code.09_palindrome_number").is_palindrome_number

def test_palindrome_true():
    assert is_palindrome_number(121) is True
    assert is_palindrome_number(1221) is True
    assert is_palindrome_number(0) is True

def test_palindrome_false():
    assert is_palindrome_number(123) is False
    assert is_palindrome_number(-121) is False

if __name__ == "__main__":
    test_palindrome_true()
    test_palindrome_false()
    print("All test cases passed.")
