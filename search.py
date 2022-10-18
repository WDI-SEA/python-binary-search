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

# ## # ## # ## # ## #
# BINARY SEARCH

def binary_search():
    nums = [0, 4, 6, 9, 15, 21, 36, 44, 51, 69]
    target = 36
    start = 0
    end = len(nums)- 1
    # print(f'start: {start}, mid: {mid}, end: {end}, target: {target}')
    while start <= end:
        mid = (start + end) // 2 # // is for floor division to avoid floats
        if nums[mid] == target:
            print(f'target: {target} is at nums array index: {mid}')
            return mid
        elif (nums[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return -1
        
# binary_search()



# ## # ## # ## # ## #
# RECURSION

def recursive_search(nums, start, end, target):
    if end >= start: # check base case
        mid = (start + end) // 2
        if nums[mid] == target: # if target is equal to mid
            return mid
        elif nums[mid] > target: # if target is less than mid, get rid of array i's > mid
            return recursive_search(nums, start, mid - 1, target)
        else: # if target > mid, get rid of array i's < mid
            return recursive_search(nums, mid + 1, end, target)
    return -1 # target is not in nums array 


nums = [0, 4, 6, 9, 15, 21, 36, 44, 51, 69]
target = 4

answer = recursive_search(nums, 0, len(nums) - 1, target)

if answer != -1:
    print('Target is at index', str(answer))
else:
    print('Target is not in nums array')


    