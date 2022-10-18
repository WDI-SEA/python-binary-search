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

# ex 1:
nums = [-1, 0, 3, 5, 9, 12]

idx = -1
def search(list, n):
    l = 0
    u = len(list) - 1

    while 1 <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['idx'] = mid
            return True
        else: 
            if list[mid] < n:
                l = mid + 1
            else: 
                u = mid - 1
    return False

list = nums
n = -1

if search(list, n):
    print('found @ index:', idx)
else:
    print('not found')
