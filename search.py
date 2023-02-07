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

# we would need a function taking in parameters(prob taking in an array, and a target)

# def binary(array, target)

# in this function i think an if, elif, else would be the thing to use in this, basically if center is equal to target, if center is greater than target, focus on right, and vice versa

# from videos, in order to get midpoint, we would need to add endpoints and divide by 2

# when after finding midpoint and seeing if greater or equal, grab new end points and make new midpoint



# _____________weston way to do it_______________
def binary(array, target):
    # state values to keep track of our windows range
    # low index of the range -- will start at 0 
    low = 0
    # high index of the range -- last index of the array
    high = len(array)
    # middle point index of the range -- start off as half the high index
    middle = high // 2

    # we may have some edge cases around the target being at index 0 or the last item
    if array[low] == target:
        return low

    # iterate until -- stop when distance is 0, or middle point equals low or high
    while low != middle:
        print(f'low: {low}, mid: {middle}, high: {high}')
        # check if the value of our middle point is equal to the target
        if array[middle] == target:
            # if so, return middle point
            return middle
        elif target < array[middle]:
            # else if, the target is less than the value at the middle point, slide the window down(to the left)
            high = middle
        else:
            # else if, the target is greater than the value at the middle, we slide the window right (up)
            low = middle


            # recalculate the middle point
        distance = high - low 
        middle = low + (distance // 2)
                # possibly break the loop if needed

    # if the loop breaks, we have not found the target
    return -1

array = [-1, 0, 3, 5, 9, 12, 15]
target = 0
print(binary(array, target))
    
