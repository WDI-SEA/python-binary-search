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

# Function takes four parameters: the array (arr), the search value (val), the starting index (start), and the ending index (end).
def binary_search(arr, val, start = 0, end = None):
    arr = arr
    val = val
    start = start
    end = end

    # Inside your function, you must detect if end is null. If it is, you need to then set it to arr.length - 1 so it holds the last index in the array.
    if end == None:
        end = len(arr) - 1

    # Find the index midway between start and end. (Not important if it isn't exactly midway.)
    mid = int(start + end / 2)

    # If it matches, return that index (mid).
    if  arr[mid] == val:
        print(arr[mid])
        return mid

    # If the value at mid is greater than val then recurse on the left half of the array.
    if arr[mid] > val:
        print(arr[mid])
        return binary_search(arr, val, start, end = mid - 1)

    if arr[mid] < val:
        print(arr[mid])
        return binary_search(arr, val, start = mid + 1, end = end)

    

nums = [-1, 0, 3, 5, 9, 12] 

binary_search(nums, 9)