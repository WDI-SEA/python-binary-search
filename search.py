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

[0, 1, 2, 3, 4, 5, 6]
[3, 4, 5, 6]


def binary_search(nums, target):
    # state values to keep track of our windows range
    # low index of the range -- will start as 0
    low = 0
    # high index of the range -- last index of the array
    high = len(nums)
    # middle point index of the range -- start off as half the high index
    middle = high // 2

    # we may have some edge cases around the target being at index 0 or the last item
    if nums[low] == target:
        return low


    # iterate until -- stop when distance is 0, or middle point equals low or high
    while low != middle:
        print(f'low: {low}, mid: {middle}, high: {high}')
        # check if the value at our middle point is equal to the target
        if nums[middle] == target:
            # if so, return middle point
            return middle
        elif target < nums[middle]:
            # else if, the target is less than the value at the middle point, 
            # slide the window down (to the left)
            high = middle
        else:
            # else if, the target is greater than the value at the middle, we slide the window right (or up)
            low = middle
        

        # recalculate the middle point
        distance = high - low
        middle = low + (distance // 2)
    
    # if the loop breaks, we have not found the target
    return -1

nums = [-1, 0, 3, 5, 9, 12] 
target = 9
# print(binary_search(nums, target)) # 4

# nums = [-1, 0, 3, 5, 9, 12]
# target = 2
# print(binary_search(nums, target)) # -1


nums = [-1, 0, 3, 5, 9, 12] 
target = 12
print(binary_search(nums, target)) # 5


# nums = [-1, 0, 3, 5, 9, 12]
# target = -1
# print(binary_search(nums, target)) # 0