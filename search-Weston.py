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
# middle index = low index + (distance // 2)

def binary_search(nums, target):
    # keep track of the window -- start by assuming the entire list is the window 
    # need variables for low index of the window, high index of the window, middle point index of the window 
    low = 0
    high = len(nums)
    mid = high // 2
    print(f"target: {target}")
    # continously iterate until the target is found or until we determine the target cannot be found
    while True:
        # check the value at the midpoint against the target, stop iterating if target is found
        if nums[mid] == target:
            return mid
        # if the value at the midpoint is greater than the target, slide the window to the left
        elif nums[mid] > target:
            high = mid
            difference = high - low
            mid = low + (difference // 2)
        # otherwise slide to the right
        else:
            low = mid
            difference = high - low
            mid = low + (difference // 2)
        print(f"low: {low}, mid: {mid}, high: {high}")
        # stop iteration when the midpoint is equal to the low or high, because we did not find it
        if mid <= low or mid >= high:
            return -1
        

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary_search(nums, target))