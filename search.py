"""
Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    
       

Output: 4
Explanation: 9 exists in nums and its index is 4
    def binary_search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
def binary_search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

Output: -1
Explanation: 2 does not exist in nums so return -1

Example 3:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 12
    def binary_search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid


Output: 5
Explanation: 12 exists in the list and its index is 5

Example 4:
Input: nums = [-1, 0, 3, 5, 9, 12], target = -1
    def binary_search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
Output: 0
Explanation: -1 exists in the list and its index is 0
"""


def binary_search(nums, target):
    # state values to keep trck of our windows range
    # low index of the range -- will start as 0
    low = 0
    # high index of the range -- will start as the last index of the array
    high = len(nums) 
    # middle point of the range -- start off as half the high index
    middle = high // 2
    # 
    # we mau have some edge cases around the target being at index 0 or the last item
    # iterate until -- stop when distance is 0, or middle point equals low or high
    while low != middle:
    # # check if the middle point is the target 
         if nums[middle] == target:
            return middle 
    # if it is, return the middle point
    # else if, the target is less than the value a the middle point, slide the window 
    # down (to the left
         elif target < nums[middle]:
            high = middle 
         else:
            low = middle   
    # else if, the target is greater than the value at the middle point, slide the window up (to the right)

    # recalculate the middle point
    distance = high - low
    middle = low + (distance // 2)
    # possibly break the loop if needed
    return -1  


nums = [-1, 0, 3, 5, 9, 12] 
target = 9
print(binary_search(nums, target))


# nums = [-1, 0, 3, 5, 9, 12] 
# target = 2
# print(binary_search(nums, target))


# nums = [-1, 0, 3, 5, 9, 12] 
# target = -1
# print(binary_search(nums, target))


# nums = [-1, 0, 3, 5, 9, 12] 
# target = 12
# print(binary_search(nums, target))