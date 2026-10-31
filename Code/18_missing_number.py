def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5, 6]))
