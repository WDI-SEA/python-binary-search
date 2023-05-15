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

# def binary_search(arr, target):
    # # keep track of minimum of the range
    # min_idx = 0
    # # keep track of the max of the range
    # max_idx = len(arr) - 1

    # # loop this until value is found, or where index would be
    # while min_idx < max_idx:
    #     # keep track of the middle of the range
    #     mid_idx = int((min_idx + max_idx) / 2)
    #     middle = arr[mid_idx]
    #     # check if middle of the range equals target
    #     if middle == target:
    #         return mid_idx
    #     # if mid < target, narrow in on right side
    #     elif middle < target:
    #         min_idx = mid_idx + 1
    #         # print(arr[mid_idx])
    #     # if mid > target, narrow in on left half
    #     else:
    #         max_idx = mid_idx - 1
    #         # print(arr[mid_idx])
    # # returns -1 if target not found in array
    # return -1

def binary_search(nums, target):
    # keep track of the window -- start by assuming the entire list is the window
    # vars for low idx of window, high idx of window, mid idx of window
    low = 0
    high = len(nums)
    mid = high // 2

    if target == nums[0]:
        return 0

    # continue to iterate until the target is found or is not here
    while True:
        # check the value at mid idx against target, stop if equal
        if nums[mid] == target:
            return mid
        # if the value at the mid idx is less than target, slide window left
        elif nums[mid] > target:
            high = mid
            difference = high - low
            mid = low + (difference // 2)
        # otherwise slid to right
        else:
            low = mid
            difference = high - low
            mid = low + (difference // 2)
    print(f"low: {low}, mid: {mid}, high: {high}")
    # stop iteration when the mid value is equal to low or high becasue we did not find it
    if mid <= low or mid >= high:
        return -1

print(binary_search([-1, 0, 3, 5, 9, 12], 2))

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