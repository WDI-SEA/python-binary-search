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

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9

# def find_index(n, t):
#     min = 0
#     max = len(n) - 1

#     while min != max:
#         mid = int((min + max) / 2)
#         if t == n[mid]:
#             return mid
#         elif t < n[mid]:
#             max = mid - 1
#             if min == max and nums[min] == t:
#                 return min
#         elif t > n[mid]:
#             min = mid + 1
#             if min == max and nums[max] == t:
#                 return max
#     return -1

# print(find_index(nums, target))
    
### RECURSIVE ###

nums_array = [-1, 0, 3, 5, 9, 12]
target_num = 9

def find_index(nums, target):
    min = 0
    max = len(nums) - 1
    mid = int((min + max) / 2)
    print(mid)
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        print (nums > nums[mid])
        # find_index(nums[mid], target)
    elif target > nums[mid]:
        print (nums < nums[mid])
        # find_index(nums[mid], target)
    # while min != max:
        
    #     if t == n[mid]:
    #         return mid
    #     elif t < n[mid]:
    #         max = mid - 1
    #         if min == max and nums[min] == t:
    #             return min
    #     elif t > n[mid]:
    #         min = mid + 1
    #         if min == max and nums[max] == t:
    #             return max
    # return -1

find_index(nums_array, target_num)