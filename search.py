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

import math

nums = [-1, 0, 3, 5, 9, 12]


def binary_search(num_input, target):
    low = 0
    high = len(num_input)
    midpoint = math.floor((low + high) / 2)
    end_result = 0
    
    while end_result == 0:
        if target == num_input[midpoint]:
            end_result += 2
        if target > num_input[midpoint]:
            low = midpoint
            midpoint = int((high+low)/2)
        elif target < num_input[midpoint]:
            high = midpoint
            midpoint = int((high+low)/2)
        if target is not num_input[midpoint] and high-low == 1 or high-low == 0:
            end_result += 1
        
    
    
    if end_result == 1:
        return f'target is not in the array, returning {-1}'
    if end_result > 1:
        return f'{target} is in the list and its index is {midpoint}'
    

print(binary_search(nums, -1))