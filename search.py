
def binary_search(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]

target = 9
print(binary_search(nums, target))  # Output: 4

target = 2
print(binary_search(nums, target))  # Output: -1

target = 12
print(binary_search(nums, target))  # Output: 5

target = -1
print(binary_search(nums, target))  # Output: 0

