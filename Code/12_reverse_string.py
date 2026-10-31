def reverse_string(s):
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)

if __name__ == "__main__":
    print(reverse_string("DevOps"))
