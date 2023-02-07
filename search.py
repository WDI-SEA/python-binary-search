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

nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
nums3 = [-1, 0, 3, 5, 9, 12]
target3 = 12
nums4 = [-1, 0, 3, 5, 9, 12]
target4 = -1



# def binary_search(nums, target, orig_nums):
#   test_index = len(nums) // 2
#   test_value = nums[test_index]
#   if test_value == target:
#     return test_value
#   elif test_index == 0:
#     return -1
#   elif len(nums) == 2:
#     if nums[0] == target:
#       return nums[0]
#     else:
#       return -1
#   elif test_value < target:
#     start_index = test_index + 1
#     return binary_search(nums[start_index:], target, orig_nums)
#   else:
#     end_index = test_index - 1
#     return binary_search(nums[:end_index], target, orig_nums)

def binary_search(nums, target):
  test_index = len(nums) // 2
  if len(nums) == 1:
    return test_index if nums[test_index] == target else -1
  elif nums[test_index] == target:
      return test_index
  else:
      if nums[test_index] < target:
          callback_response = binary_search((nums[test_index:]), target)
          return test_index + callback_response if callback_response != -1 else -1
      else:
          return binary_search((nums[:test_index]), target)
  
  
print(binary_search(nums1, target1))
print(binary_search(nums2, target2))
print(binary_search(nums3, target3))
print(binary_search(nums4, target4))