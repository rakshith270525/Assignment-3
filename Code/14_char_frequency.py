def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

if __name__ == "__main__":
    print(char_frequency("banana"))
