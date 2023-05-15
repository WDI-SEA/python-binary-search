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


# import math 
# # I want to create a function thats uses binary search to find the index of 9 in the array.

# def binary_search(nums, target):
#     start = 0
#     end = len(nums)-1
#     length = len(nums)
#     total = sum(nums)
#     average = total / length
#     average = math.floor(average)
#     print(f'number of item in array is {length} the sum of those numbers is {total} and the average is {average}')
#     print(f'here is the min{min}')
#     if average == target:
#         print("target found")
#     elif average < target:
#         target + 1
#     elif average >
   
        

# let min= 0 and max = -1

#compute guess as the average of max and min rounded down(so that its an integer)
   # guess = 

# binary_search([-1, 0, 3, 5, 9, 12], 9)


#if array[guess] = target then stop- return guess

#if the guess was too low that is array[guess] < target, then set min = guess + 1 otherwise if too high set max = guess - 1.


# def b_search(nums, target):
#     min = 0
#     max = len(nums) - 1

#     while min <= max:
#         mid = (max - min) / 2
#         if mid == target:
#             return mid
#         if mid < target:
#             min = mid + 1
#         else:
#             max = mid - 1
#     return -1 

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9

# result= b_search(nums, target)

# if result != -1:
#     print(f"target found at index {result}")
# else:
#     print('target not found in the array')

#didtance = high index - low index
# mid index = low index + (distance //2)

def binary_search(nums, target):
    # keep track of the  window. stat by assuming that the entire list is the window
    # variable for the low index of the window, hight index of the window, middle point index of the window.

    low = 0
    high = len(nums)
    mid = high // 2

    if target == nums[0]:
        return 0

    #continuouly iterate untill the target is found fo we determin that the target cannot be found
    while True:
        #check the value at the mid point agianst the target, stop iterating if the target is found
        if nums[mid] == target:
            return mid
        #if the value at the mid point is less than the taregt slide the window to the left
        elif nums[mid] > target:
            high = mid
            difference = high - low
            mid = low + (difference // 2)
      
        else:
            low = mid
            difference = high - low 
            mid = low +( difference // 2)
        print(f"low:{low} mid:{mid} high{high}")

        # stop iteration when the mid point is = low or high because we did not finde it
        if low == mid:
            return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 11
print(binary_search(nums, target))