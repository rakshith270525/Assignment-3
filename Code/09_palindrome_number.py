def is_palindrome_number(n):
    if n < 0:
        return False
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return original == rev

if __name__ == "__main__":
    print(is_palindrome_number(121))
    print(is_palindrome_number(123))
