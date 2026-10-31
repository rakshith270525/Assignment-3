def count_vowels_consonants(text):
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

if __name__ == "__main__":
    print(count_vowels_consonants("Hello World"))
