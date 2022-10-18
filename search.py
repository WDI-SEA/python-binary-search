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



# nums = [-1, 0, 3, 5, 9, 12]

# target = 9

# low = int(nums[0])
# high = int(nums[len(nums)-1])

# mid = math.floor((low + high)/2)

# print(mid)

# for index,char in enumerate(nums):
#     print(char, index)
#     low = index

li = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

def binarySearch(listData, value): #takes in two arguments, the list and a value
    low = 0 #start at index 0
    high = len(listData) - 1 #start at the length of the list -1 (this will give the index of the highest number bc low starts at 0)
    while (low <= high):
        mid = math.floor((low + high)/2) # need to round down bc mid can sometimes be a float
        if (int(listData[mid]) == value):
            return mid 
        elif (int(listData[mid]) < value):
            low = mid + 1 #this becomes the new low
        else: #otherwise if the value is greater than
            high = mid - 1 #this becomes the new high
    return -1

print(binarySearch(li, 17))