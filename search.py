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

import math



# nums = [-1, 0, 3, 5, 9, 12]

# target = 9

# low = int(nums[0])
# high = int(nums[len(nums)-1])

# mid = math.floor((low + high)/2)

# print(mid)

# for index,char in enumerate(nums):
#     print(char, index)
#     low = index

li = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

# def binarySearch(listData, value): #takes in two arguments, the list and a value
#     low = 0 #start at index 0
#     high = len(listData) - 1 #start at the length of the list -1 (this will give the index of the highest number bc low starts at 0)
#     while (low <= high):
#         mid = math.floor((low + high)/2) # need to round down bc mid can sometimes be a float
#         if (int(listData[mid]) == value):
#             return mid 
#         elif (int(listData[mid]) < value):
#             print(int(listData[low]), int(listData[high]))
#             low = mid + 1 #this becomes the new low
#         else: #otherwise if the value is greater than
#             print(int(listData[low]), int(listData[high]))
#             high = mid - 1 #this becomes the new high
#     return -1

# print(binarySearch(li, 17))

# DELIVERABLE REVIEW

def binary_search(nums, target):
    # keep track of range
    # high point index
    high = len(nums)
    # low point index
    low = 0
    # mid point index
    mid = high // 2

    # might edge case handling for first and last valies in the list
    if nums[low] == target:
        return low
    # loop until we have found the target or determined the target isn't here
    while True:
        # check if midpoint is the target
        if nums[mid] == target: 
            # if so, we can return midpoint
            return mid
        # if the midpoint is less than the target,
        elif nums[mid] < target: 
            # slide right by making low equal to mid
            low = mid
            # recalc the new mid
        # if the midpoint is greater than the target,
        else:
            # slide left by making high equal to mid
            high = mid
            # recalc the new mid
        distance = high - low
        mid = low + (distance // 2)

        print(f'high: {high}, low: {low}, mid: {mid}')
        #determine if we are out of bounds after recalculating the middle point
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

