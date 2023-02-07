"""
Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

import math
nums = [-1, 0, 3, 5, 9, 12]
target = 4
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high: 
        mid = (low + high) / 2
        mid = math.floor(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            return -1
print(search(nums, target)) 


Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1




Example 3:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 12
Output: 5
Explanation: 12 exists in the list and its index is 5
import math
nums = [-1, 0, 3, 5, 9, 12]
target = 4
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high: 
        mid = (low + high) / 2
        mid = math.floor(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            return -1
print(search(nums, target)) 



Example 4:
Input: nums = [-1, 0, 3, 5, 9, 12], target = -1
Output: 0
Explanation: -1 exists in the list and its index is 0
import math
nums = [-1, 0, 3, 5, 9, 12]
target = 4
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high: 
        mid = (low + high) / 2
        mid = math.floor(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            return -1
print(search(nums, target)) 
"""

import math
nums = [-1, 0, 3, 5, 9, 12]
target = -1
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high: 
        mid = (low + high) / 2
        mid = math.floor(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(search(nums, target)) 
       
