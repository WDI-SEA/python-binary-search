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


def binary_search(nums, target):
    # keep track of range
    # high point index
    high = len(nums)
    # low point index
    low = 0
    # mid point index
    mid = high // 2

    # might need edge case handling for first and last values in the list 

    # loop until we have found the target or we have determined the target is not here

        # check if the mid point is the target number 
            # if so, we can return mid point
        # if the mid point is less than the target
            # slide right by making low equal to mid
            # recalc the new mid
        # if the mid point is greater than the target
            # slide right by making high equal to what mid currently is
            # recalc the new mild

        # determine if we are out of bounds after recalculating the middle point
            # if we are -- return -1 since our target is not present