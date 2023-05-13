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

def binary_search(arr):
    min_idx = arr[0]
    max_idx = len(arr) - 1
    mid_idx = int(max_idx / 2)
    middle = arr[mid_idx]
    
    print(min_idx)
    print(mid_idx)
    print(middle)
    print(max_idx)

binary_search([-1,2,4,6,8])