def second_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]

if __name__ == "__main__":
    print(second_largest([10, 20, 4, 45, 99]))
