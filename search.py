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
#         mid = (min + max) // 2
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

def binary_search(nums, target, low = None, high = None):
    # if this is the first recursion, set high and low to be the whole list of nums
    if high == None:
        high = len(nums)
        low = 0

    # calculate the mid
    distance = high - low    
    mid = low + (distance // 2)
    # base case -- we found the target, or decided the target is not here
    if nums[mid] == target:
        return mid
    elif mid == low:
        return -1
    #recursive cases -- we need to move the range up or down
    # if mid is greater than target
    elif nums[mid] > target:
        # move the window left
        return binary_search(nums, target, low, mid)
    # if mid is less than target
    else:
        return binary_search(nums, target, mid, high)
        # move the window right


nums = [-1, 0, 3, 5, 9, 12]
target = -1

print('should be 0:', binary_search(nums, target))



# nums_array = [-1, 0, 3, 5, 9, 12]
# target_num = 0

# def find_index(nums, target, min, max):
#     mid = int((min + max) / 2)
#     if mid == max or mid == min:
#         return -1
#     else:
#         mid = (min + max) // 2

#         if target == nums[mid]:
#             return mid
#         elif target > nums[mid]:
#             return find_index(nums, target, (mid + 1), max)
#         else:
#             return find_index(nums, target, min, (mid - 1))

# print(find_index(nums_array, target_num, 0, (len(nums_array) -1)))