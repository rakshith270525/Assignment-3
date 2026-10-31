import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
primes_in_range = importlib.import_module("Code.07_primes_in_range").primes_in_range

def test_standard_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]
    assert primes_in_range(10, 20) == [11, 13, 17, 19]

def test_empty_range():
    assert primes_in_range(24, 28) == []
    assert primes_in_range(-10, 1) == []

if __name__ == "__main__":
    test_standard_range()
    test_empty_range()
    print("All test cases passed.")
