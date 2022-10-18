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
    if nums[low] == target:
        return low
    # loop until we have found the target or we have determined the target is not here
    while True:
        # check if the mid point is the target number 
        if nums[mid] == target:
            # if so, we can return mid point
            return mid
        # if the mid point is less than the target
        elif nums[mid] < target:
            # slide right by making low equal to mid
            low = mid
            # recalc the new mid
        # if the mid point is greater than the target
        else:
            # slide right by making high equal to what mid currently is
            high = mid
            # recalc the new mild

          # recalc the new mid
        distance = high - low
        mid = low + (distance // 2)

        # print(f'high: {high}, low: {low}, mid: {mid}')

        # determine if we are out of bounds after recalculating the middle point
        if low == mid:
            # if we are -- return -1 since our target is not present
            return -1


nums = [-1, 0, 3, 5, 9, 12] 
target = 9

print('it should be 4:', binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 12
print('it should be 5:', binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = -50
print('it should be -1:', binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = -1
print('it should be 0:', binary_search(nums, target))