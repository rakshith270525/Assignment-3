def is_palindrome_string(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(is_palindrome_string("madam"))
    print(is_palindrome_string("hello"))
