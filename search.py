# distance = high index - low index
# middle index = low index + (distance // 2)

def binary_search(nums, target):
    # keep track of the window -- start by assuming the entire list is the window
    # vars for low index of the window, high index of the window, middle point index of the window
    low = 0
    high = len(nums)
    mid = high // 2

    # account for case where target is first in the list
    if target == nums[0]:
        return 0

    # continously iterate until the target is found or we determine that the target cannot be found
    while True:

        # check the value at the midpoint against the target, stop iterating if target is found
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

        print(f"low: {low}, mid: {mid}, high: {high}")
        # stop iteration when the midpoint is equal to low or high, becase we did not find it
        if low == mid:
            return -1
        

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

nums = [-1, 0, 3, 5, 9, 12]
target = 9

nums = [-1, 0, 3, 5, 9, 12]
target = 2

nums = [-1, 0, 3, 5, 9, 12]
target = 12

nums = [-1, 0, 3, 5, 9, 12]
target = -2

print(binary_search(nums, target))