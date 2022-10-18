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
#     # keep track of range -- start by assuming the entire list of nums is our range
#     # high point index
#     high = len(nums)
#     # low point index
#     low = 0
#     # mid point index
#     mid = high // 2

#     # might need edge case handling for first and last values in the list
#     if nums[low] == target:
#         return low
#     # loop until we have found the target or determined the target isn't here
#     while True:
#         # check if the mid point is the target
#         if nums[mid] == target:
#             # if so, we can return mid point
#             return mid
#         # if the mid point is less than the target
#         elif nums[mid] < target:
#             #  slide right by making low equal to mid
#             low = mid
#             # recalc the new mid
#         # if the mid point is greater than the target
#         else:
#             # slide right by making high equal to what mid currently is
#             high = mid
#             # recalc the new mid

#         # recalc the new mid
#         distance = high - low
#         mid = low + (distance // 2)

#         # print(f'high: {high}, low: {low}, mid: {mid}')

#         # determine if we are out of bounds after recalculating the middle point
#         if low == mid:
#             # if we are -- return -1 since our target is not present
#             return -1

# recursive solve
def binary_search(nums, target, low = None, high = None):
    # if this is the first recurstion, set high an low to be the whole list of nums
    if high == None:
        high = len(nums)
        low = 0
    
    # calculate the mid
    distance = high - low
    mid = low + (distance // 2)
    print(f'low: {low}, mid: {mid}, high: {high}')
    # base case -- we have found the target, or decided the targets not here
    if nums[mid] == target:
        return mid
    elif mid == low:
        return -1
    # recursive cases -- we need to move the range down or up
    # if mid is greater than target
    elif nums[mid] > target:
        # move window left
        return binary_search(nums, target, low, mid)
    # if mid is less than target, move window right
    else:
        return binary_search(nums, target, mid, high)

# nums = [-1, 0, 3, 5, 9, 12] 
# target = 5

# print('it should be 3:', binary_search(nums, target))

# nums = [-1, 0, 3, 5, 9, 12]
# target = 12
# print('it should be 5:', binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 4
print('it should be -1:', binary_search(nums, target))

# nums = [-1, 0, 3, 5, 9, 12]
# target = -1
# print('it should be 0:', binary_search(nums, target))