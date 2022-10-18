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

# Binary Search

def binary_search(nums, target):
    # keep track of range -- start by assuming the entire list of nums is our range
    # high point index
    high = len(nums)
    # low point index
    low = 0
    # mid point index
    mid = high // 2 #force integer division each time

    # might edge case handling for first and last values in the list

    # loop until until we have found target or we determined.. the target isn't here
    while True:
        # check if midpoint is target, we return index of mid point
        if nums[mid] == target:
            # if if so we can return the mid point
            return mid
        # if the mid point is less than the target
        elif nums[mid] < target:
            # slide right by making low = to mid
            low = mid
            # recalc the new mid
        # if the mid point is greater than the target
        else:
            # slide right by making the high equal to what mid currently is
            high = mid
            # recalc the new mid

        # recalc the new mid
        distance = high - low
        mid = low + (distance // 2)
        
        # determine if we are out of bounds after recalculating the middlepoint
            # if we are -- return -1 since our target is not present

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print('it should be 4:', binary_search(nums, target))


nums = [-1, 0, 3, 5, 9, 12]
target = 12
print('it should be 12:', binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
print('it should be -1:', binary_search(nums, target))