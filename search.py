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
nums = [-1, 0, 3, 5, 9, 12, 15, 20, 33, 40]
output = -5
low = nums[0]
high = nums[len(nums) - 1]
middle_idx = math.trunc((len(nums)-1)/2)
middle = nums[middle_idx]

def binary_search ():
    global nums
    global output
    global low
    global high
    global middle_idx
    global middle
    # print(middle)
    target = int(input("give us a target number to search for: \n"))

    if target == low:
        output = 0
    elif target == high:
        output = len(nums) - 1
    elif target < low or target > high:
        output = -1
    else:
        def search():
            global output
            global low
            global high
            global middle_idx
            global middle
            if target == middle:
                output = middle_idx
            elif nums.index(high) - nums.index(low) == 1:
                output = -1
            else:
                if target < middle:
                    high = middle
                    middle_idx = math.trunc(nums.index(high)/2)
                    middle = nums[middle_idx]
                    search()
                else: 
                    low = middle
                    middle_idx = middle_idx + math.trunc((nums.index(high) - nums.index(low))/2)
                    middle = nums[middle_idx]
                    search()
        search()

    print(f"Output: {output}")
    if output == -1:
        print(f"Explanation: {target} does not exist in nums so return -1 ")
    elif output == -5:
        print("error has occured")
    else:         
        print(f"Explanation: {target} exists in the list and its index is {output} ")

binary_search()

    

