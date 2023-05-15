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

def binary_search(list, target):
    window_start = 0
    while True:
        if len(list) == 0:
            return -1
        midpoint = math.floor(len(list) / 2)
        if list[midpoint] == target:
            return f"{target} found at list index {midpoint + window_start}"
        elif list[midpoint] > target:
            list = list[slice(0, midpoint)]
        elif list[midpoint] < target:
            prev_length = len(list)
            list = list[slice(midpoint + 1, len(list))]
            window_start = window_start + prev_length - len(list)

myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 22, 26, 54, 433, 3422, 5555, 6666, 344444, 5757575757]

myTarget = 55

print(binary_search(myList, myTarget))