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


# need a low, mid, high where mid is (high - low)/2 (-1)
# check to see if x is higher or lower than that mid number
# if x is greater, ignore values to the left
# if x is lower, ignore values to the right 
# or x = mid value, we stop
# if not, we keep going


def binary(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) / 2 

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1 

        else: 
            return mid

    return -1

arr = [ 1, 3, 5, 7, 9]
x = 3

result = binary(arr, x)

if result != -1:
    print (result)