import math

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

def BinarySearch(n):
    nums = [-1, 0, 3, 5, 9, 12]
    low = 0
    high = len(nums) - 1
    middle = math.floor((high+low)/2)

    while (low <= middle):
        if(nums[middle] == n):
            print(f'The number {nums[middle]} is in index {middle}')
            break  
        elif(low == middle and nums[middle] == n):
            print(f'The number {nums[middle]} is in index {middle}')
            break
        elif(low == middle and nums[high] == n):
            print(f'The number {nums[high]} is in index {high}')
            break
        elif(high == middle and (nums[middle] == n)):
            print(f'The number {nums[middle]} is in index {middle}')
            break  
        elif(high == middle and (nums[low] == n)):
            print(f'The number {nums[low]} is in index {low}')
            break  
        elif(low == middle and nums[middle] != n):
            print(f'The number {n} is not in this list. Ouput -1')
            return -1
        elif(high == middle and nums[middle] != n):
            print(f'The number {n} is not in this list. Output -1')
            return -1
        elif(nums[middle] < n):
            low = middle + 1
            # print('low low', low)
            middle = math.floor((high+low)/2)
            # print('low middle', middle)
        elif(nums[middle] > n):
            high = middle - 1
            # print('high high', high)
            middle = math.floor((high+low)/2)
            # print('high middle', middle)


BinarySearch(2)

# tested with -1,0,3,5,9,12,2,13,-2


