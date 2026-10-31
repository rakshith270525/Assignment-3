import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
count_vowels_consonants = importlib.import_module("Code.11_vowels_consonants").count_vowels_consonants

def test_counts():
    assert count_vowels_consonants("Hello World") == (3, 7)
    assert count_vowels_consonants("AEIOU") == (5, 0)
    assert count_vowels_consonants("123 !@#") == (0, 0)

if __name__ == "__main__":
    test_counts()
    print("All test cases passed.")
