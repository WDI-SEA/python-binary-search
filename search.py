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

    high = len(nums)

    low = 0

    mid = high // 2

    while True:
        if nums[mid] == target:

            return mid

        elif nums[mid] < target:

            low = mid

        else:

            high = mid 

        distance = high - low
        mid = low + (distance // 2)


nums = [-1, 0, 3, 5, 9, 12] 
target = 9

print(binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12] 
target = 12

print( binary_search(nums, target))

nums = [-1, 0, 3, 5, 9, 12] 
target = -1

print( binary_search(nums, target))
