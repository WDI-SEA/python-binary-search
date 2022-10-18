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


# Working Search (non-recursive)

# def binary_search(nums, target):
#     low = 0
#     high = len(nums)
#     middle = int((low + high) / 2)
#     goalIsReached = 0

#     if goalIsReached == 1:
#         return f'target is not in the array, returning{-1}'

#     while goalIsReached == 0:
#         if target == nums[middle]:
#             goalIsReached += 2
#         if target > nums[middle]:
#             low = middle
#             middle = int((high+low)/2)
#         elif target < nums[middle]:
#             high = middle
#             middle = int((high+low)/2)
#         if target != nums[middle] and high-low == 1 or high-low == 0:
#             goalIsReached += 1


#     if goalIsReached == 1:
#         return f'target is not in the array, returning {-1}'
#     if goalIsReached > 1:
#         return f'{target} is in the list and its index is {middle}'


# print(binary_search([-1, 1, 3], -1))









# Recursive attempt w/ global variables

# arr = [0, 1, 3, 4, 5]
# low = 0
# high = len(arr) 
# middle = int((low + high) / 2)

# def binary_search(nums, target):
#     global low
#     global high
#     global middle

#     print(nums)
#     print(middle)

#     if target != nums[middle] and high-low == 1 or high-low == 0:
#         return f'target is not in the array, returning {-1}'
#     elif target == nums[middle]:
#         return f'{target} is in the list and its index is {middle}'

#     if target > nums[middle]:
#         low = middle
#         middle = int((high+low)/2)
#     elif target < nums[middle]:
#         high = middle
#         middle = int((high+low)/2)


#     return binary_search(nums, target)

# print(binary_search(arr, 6))







# Non-global variable recursion version

def binary_search(nums, target):
    low = 0
    high = len(nums) 
    middle = int((low + high) / 2)
    goalIsReached = 0

    print(nums)
    print(middle)

    if target != nums[middle] and high-low == 1 or high-low == 0:
        goalIsReached = 1
        return f'target is not in the array, returning {-1}'
    elif target == nums[middle]:
        goalIsReached = 2
        return f'{target} is in the list and its index is {middle}'

    if target > nums[middle]:
        low = middle
        middle = int((high+low)/2)
    elif target < nums[middle]:
        high = middle
        middle = int((high+low)/2)


    return binary_search(nums, target)

print(binary_search([0, 1, 2, 3, 4, 5, 6], 6))
