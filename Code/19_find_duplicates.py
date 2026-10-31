def find_duplicates(lst):
    seen = set()
    duplicates = []
    dup_set = set()
    for item in lst:
        if item in seen and item not in dup_set:
            duplicates.append(item)
            dup_set.add(item)
        seen.add(item)
    return duplicates

if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))
