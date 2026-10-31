import string

def word_frequency(sentence):
    cleaned = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

if __name__ == "__main__":
    print(word_frequency("hello world hello devops"))
