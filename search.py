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
# EX 1
# def binary_search(nums, target):
#     # keep track of range
#     # keep track of first "door"
#     hight = len(nums)
#     # last door
#     low = 0
#     # door in the middle
#     mid = hight // 2
#     # might need edge case hansling for first and last values in the list

#     # loop until we have found the target or determined the target isnt here
#     while True:
#         # if target is behind middle door -- return target
#         if nums[mid] == target:
#             return mid
#         # if num behing middle door is less than the target -- slide right by reasingning index of last door equal to the index of prev middle door
#         elif nums[mid] < target:
#             low = mid
#         # if num behind middle door is greater than target -- slide left by reasining index of current mid door to be first door and assiging a new middle door
#         else: 
#             high = mid
#         distance = hight - low
#         mid = low + (distance // 2)
#         # determinate if we are out of bounds after recalculating the middle point
#             # if we are -- return -1 since our target is not present
#         if low == mid:
#             return -1

# from turtle import distance


def binary_search(nums, target, low = None, high = None):
   
    if high == None:
        high = len(nums)
        low = 0

    # calculate the mid
    distance = high - low
    mid = low + (distance // 2)
    # base case -- we have found the target 
    if nums[mid] == target:
        return mid
    elif mid == low:
        return -1
    # recursive case -- we need to mode the range dowm or up
    # if mid is greater than target -- move window left
    elif nums[mid] > target: 
        return binary_search(nums, target, low, mid )
    else:
        return binary_search(nums, target, mid, high)


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print('it should be 4:', binary_search(nums, target))
# nums = [-1, 0, 3, 5, 9, 12]
# target = 12
# print('it should be 5:', binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 4
print('it should be -1:', binary_search(nums, target))