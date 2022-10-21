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

# def binary_search(nums, target):
#     # keep track of our range -- start by assuming the entire list of nums is our range.
    
#     # high point index
#     high = len(nums)
#     # low point index
#     low = 0
#     # mid point index
#     mid = high // 2
#     # potential edge case handling for first and last values in the list.
#     if nums[low] == target:
#         return low
#     # loop until we have found the target, or found that the target ins't here.
#     while True:
#         # check if the mid point is the target.
#         if nums[mid] == target:
#             # if so, we can return the mid point.
#             return mid
#         # if the mid point is less than the target.
#         elif nums[mid] < target:
#             # move to the right ( up ).
#             low = mid 
#         # if the mid point is more than the target.
#         else: 
#             # move to the left ( down ).
#             high = mid
#         # recalculate the new mid
#         distance = high - low
#         mid = low + (distance // 2)

#         print(f'high: {high}, mid: {mid}, low: {low}')

#         if low == mid:

#             return -1



# Recursive solve
def binary_search(nums, target, low = None, high = None):
    #  if this is the first recursion, set high and low to be the whole list of nums
    if high == None:
        high = len(nums)
        low = 0
    # calculate the mid
    distance = high - low
    mid = low + (distance // 2)
    print(f'low: {low}, mid: {mid}, high: {high}')
    # base case: we found the target
    if nums[mid] == target:
        return mid
    elif mid == low:
        return -1
    # recursive case: we need to move the range down or up
    # if mid greater than target
    elif nums[mid] > target:
        return binary_search(nums, target, low, mid)
    else:
        return binary_search(nums, target, mid, high)

nums = [-1, 0, 3, 5, 9, 12, 14, 15, 19, 22, 29, 32, 33, 34, 36, 43, 47, 54, 76]
target = 0

print('The actual target is: 0, and the binary_search result is: ', binary_search(nums, target))