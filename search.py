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
# setup
def binary_search(array, target):
    left = 0
    right = len(array)
# determine the middle
    while left < right:
# run through loop to half things
        middle = (left + right) // 2
        if array[middle] < target:
            left = middle + 1
        else:
            right = middle
# check for target
    if array[left] == target:
        return left
    else:
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = -1
index = binary_search(nums, target)
print(index)