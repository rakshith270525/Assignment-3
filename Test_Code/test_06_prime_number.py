import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
is_prime = importlib.import_module("Code.06_prime_number").is_prime

def test_primes():
    assert is_prime(2) is True
    assert is_prime(13) is True
    assert is_prime(29) is True

def test_non_primes():
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False
    assert is_prime(15) is False

if __name__ == "__main__":
    test_primes()
    test_non_primes()
    print("All test cases passed.")
