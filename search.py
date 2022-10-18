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
def binary_search(arr, target):
    if arr == None or len(arr) == 0:
        return -1
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = int((r - l) / 2 + l)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
def binary_search2(arr, target, start, end):
    if arr == None or len(arr) == 0:
        return -1
    if start > end:
        return -1
    mid = int((end - start) / 2 + start)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search2(arr, target, mid + 1, end)
    else:
        return binary_search2(arr, target, start, mid - 1)

    
arr = [-1, 0, 3, 5, 9, 12]
print(binary_search(arr, 9))
print(binary_search(arr, 2))
print(binary_search(arr, 12))
print(binary_search(arr, -1))
print(binary_search2(arr, 9, 0, len(arr) - 1))
print(binary_search2(arr, 2, 0, len(arr) - 1))
print(binary_search2(arr, 12, 0, len(arr) - 1))
print(binary_search2(arr, -1, 0, len(arr) - 1))