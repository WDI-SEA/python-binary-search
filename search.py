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
import math

def binary_search(nums, target):
    minimum = 0
    maximum = len(nums)-1
    while minimum <= maximum:
        raw_median = (maximum+minimum)/2
        median = math.ceil(raw_median)
    
        if nums[median] < target:
            minimum = median + 1
            print(f"incrementing {nums[median]}")
        elif nums[median] > target:
            maximum = median -1
            print(f"decrementing {nums[median]}")
        else:
            return(f"found it! {nums[median]} at index {median}")
            break
    return -1

nums = [-1, 0, 3, 5, 9, 12]

print(binary_search(nums, 9))
print(binary_search(nums, 2))
print(binary_search(nums, 12))
print(binary_search(nums, -1))

