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

def binary_Search(arr, value):
    start = 0
    end = len(arr)- 1

    while (start <= end):
        mid = (start + end) // 2
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_Search(arr, 2)) 

def recursive(arr, value, start = 0, end = len(arr)):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return recursive(arr, value, start, mid - 1)
    else:
        return recursive(arr, value, mid + 1, end)

print(recursive(arr, 2))