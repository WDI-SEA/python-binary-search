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
# for illustration purposes, the indexes of each elements are shown on the line below
li = [ 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
# idx  0  1  2  3  4   5   6   7   8   9   10  11  12  13  14  15  16

import math

def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = math.floor((low + high) / 2)
        if list[middle] == target:
            return middle
        elif list[middle] > target:
            high = middle - 1
        elif list[middle] < target:
            low = middle + 1
    return -1

print(binary_search(li, 59))