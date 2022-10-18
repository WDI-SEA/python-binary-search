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
import math

nums = [1,2,3,4,5]

arrLength = len(nums)
# print(arrLength)

def findNumber(num, arr):
    index_low = 0
    index_high = len(arr)
    def compare():
        index_middle = math.floor((index_high - index_low)/2) 
        # print(index_high)
        # print(index_middle)
        # print(index_low)
        if arr[index_middle] == num:
            return index_middle
        elif arr[index_middle] > num:
            index_high = index_middle
            return compare()
        else:
            index_low = index_middle
            return compare()

    compare()

findNumber(1, [1,2,3,4,5])
