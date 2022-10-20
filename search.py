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

def binary_search(list, target):
  # keep track of range

  # high point index
  high = len(list)

  # low point index
  low = 0

  # mid point index
  mid = high // 2

  # # might need edge case for handling first and last values in the list
  if list[low] == target:
    return low

  # loop until we have found the target or determined the target isn't here
  while True:
    # check if the mid point is the target
    if list[mid] == target:
      # if so, we can return mid point
      return mid
    # if the mid point is less than the target
    elif list[mid] < target:
      # slide right by making low equal to mid
      low = mid
    # if the mid point is greater than the target
    else:
      # slide left by making high equal to what mid currently is
      high = mid
    # recalc the new mid
    new_range = high - low
    mid = new_range // 2 + low
    
    # determine if we are out of bounds after recaclulating the middle point
    if low == mid:
      # if we are -- return -1 since our target is not present
      return -1

print(binary_search([-1, 0, 3, 5, 9, 12], 9))
print(binary_search([-1, 0, 3, 5, 9, 12], 2))
print(binary_search([-1, 0, 3, 5, 9, 12], 12))
print(binary_search([-1, 0, 3, 5, 9, 12], -1))