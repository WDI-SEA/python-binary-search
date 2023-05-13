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

def binary_search(arr, target):
    min_idx = arr[0]
    max_idx = len(arr) - 1
    mid_idx = int(max_idx / 2)
    middle = arr[mid_idx]

    # keep track of minimum of the range
    # keep track of the max of the range
    # keep track of the middle of the range
    # check if middle of the range equals target
        # if not & mid is > target, check left half, if mid < target check right half
        # loop this until value is found, or where index would be
    
    print("min idx: ", min_idx)
    print("mid idx: ", mid_idx)
    print("middle value: ", middle)
    print("max idx: ", max_idx)

binary_search([-1, 0, 3, 5, 9, 12], -1)