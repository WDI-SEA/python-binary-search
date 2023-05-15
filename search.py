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

# distance = high index - low index
# middle = low index + (distance // 2)

def binary_search(nums, target):
    # keep track of the window -- start by assuming the entire list is the window
    # vars for low index, the high index, middle point index.
    # continusly iterate until the target is found or we determine the target cannot be found
        # check the value at the mid point against the target, stop iterating if target is found.
        # if the value at the midpoint is less than the target, slide the window down.
    low = 0
    high = len(nums)
    mid = high // 2

    while True:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid
            difference = high - low
            mid = low + (difference // 2)
        else:
            low = mid
            difference = high - low
            mid = low + (difference // 2)
        print(f'low:{low}, mid:{mid}, high:{high}')
        if mid == low:
            return -1

print(binary_search([-1, 0, 3, 5, 9, 12], 9 ))
print(binary_search([-1, 0, 3, 5, 9, 12], 2 ))
print(binary_search([-1, 0, 3, 5, 9, 12], 12 ))
print(binary_search([-1, 0, 3, 5, 9, 12], -1 )) 