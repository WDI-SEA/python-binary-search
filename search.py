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


# need a low, mid, high where mid is (high - low)/2 (-1)
# check to see if x is higher or lower than that mid number
# if x is greater, ignore values to the left
# if x is lower, ignore values to the right 
# or x = mid value, we stop
# if not, we keep going


# def binary(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0

#     while low <= high:
#         mid = (high + low) / 2 

#         if arr[mid] < x:
#             low = mid + 1

#         elif arr[mid] > x:
#             high = mid - 1 

#         else: 
#             return mid

#     return -1

# arr = [ 1, 3, 5, 7, 9]
# x = 3

# result = binary(arr, x)

# if result != -1:
#     print (result)



def binary_search(nums, target):
    # keep track of range
    # high point index
    high = len(nums)
    # low point index
    low = 0
    # mid point index
    mid = high // 2

    # might need to handle edge case handling for first and last values in the list
    if nums[low] == target:
        return low

    # loop until we have found the target or determined the target isn't here
    while True:
        # check if the mid point is the target
        if nums[mid] == target:
            # if so, we can return mid point
            return mid
        # if the midpoint is less than the target
        elif nums[mid] < target:
            # slide right by making low equal to mid 
            low = mid
            # recalc the new mid 
        # if the mid point is greater than the target 
        else: 
            # slide right by making high equal to mid currently is
            high = mid
            # recalc the new mid 

        # recalc the new mid
        distance = high - low
        mid = low + (distance // 2)

        # determine if we are out of bounds after recalculating the middle point
        if low == mid:
            # if we are -- return -1 since our target is not present
            return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print ('it should be 4', binary_search(nums, target))