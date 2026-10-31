def common_elements(list1, list2):
    set2 = set(list2)
    seen = set()
    common = []
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            common.append(item)
    return common

if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
