"""
Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Example 3:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 12
Output: 5
Explanation: 12 exists in the list and its index is 5

Example 4:
Input: nums = [-1, 0, 3, 5, 9, 12], target = -1
Output: 0
Explanation: -1 exists in the list and its index is 0
"""

def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    while (start <= end):
        midpoint = (start + end) // 2
        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
print(binary_search(nums, 9))     # expect 4
print(binary_search(nums, 2))     # expect -1
print(binary_search(nums, 12))    # expect 5
print(binary_search(nums, -1))    # expect 0

print("----")

def recursive_binary_search(nums, target, start, end):
    if start > end:
        return -1
    midpoint = (start + end) // 2
    if nums[midpoint] == target:
        return midpoint
    elif nums[midpoint] > target:
        return recursive_binary_search(nums, target, start, midpoint - 1)
    else:
        return recursive_binary_search(nums, target, midpoint + 1, end)

print(recursive_binary_search(nums, 9, 0, len(nums)))     # expect 4
print(recursive_binary_search(nums, 2, 0, len(nums)))     # expect -1
print(recursive_binary_search(nums, 12, 0, len(nums)))    # expect 5
print(recursive_binary_search(nums, -1, 0, len(nums)))    # expect 0
