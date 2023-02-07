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
# def binary_search(arr, val, start = 0, end = None):
#     arr = arr
#     val = val
#     start = start
#     end = end

#     # Inside your function, you must detect if end is null. If it is, you need to then set it to arr.length - 1 so it holds the last index in the array.
#     if end == None:
#         end = len(arr) - 1

#     # Find the index midway between start and end. (Not important if it isn't exactly midway.)
#     mid = int(start + end / 2)

#     # If it matches, return that index (mid).
#     if  arr[mid] == val:
#         print(arr[mid])
#         return mid

#     # If the value at mid is greater than val then recurse on the left half of the array.
#     if arr[mid] > val:
#         print(arr[mid])
#         return binary_search(arr, val, start, end = mid - 1)

#     if arr[mid] < val:
#         print(arr[mid])
#         return binary_search(arr, val, start = mid + 1, end = end)

    

# nums = [-1, 0, 3, 5, 9, 12] 

# binary_search(nums, 9)

def binary_search(nums, target):
    # state values to keep track of our windows range
    # low index of the range -- will start as 0
    low = 0
    # high index of the range -- last index of the array
    high = len(nums)
    # middle point index of the range -- start off as half the index
    middle = high // 2

    # we may have some edge cases around the target being at index 0 or the last item
    if nums[low] == target:
        return low

    # we may have some edge cases around the target being at index 0 or the last item

    # iterate until -- stop when distance is 0, or middle point equals low or high
    while low != middle:
        # check if the value at our middle point is equal to the target
        if nums[middle] == target:
            # if so, return middle point
            return middle
        # else if, the target is less than the value at the middle point, slide the window down (to the left)
        elif target < nums[middle]:
            high = middle
        # else if, the target is greater than the value at the middle, we slide the window right (or up)
        else:
            low = middle

        # recalculate the middle point
        distance = high - low
        middle = low + (distance // 2)
        
    # if the loop breaks, we have not found the target
    return -1

# nums = [-1, 0, 3, 5, 9, 12] # target = 9

# nums = [-1, 0, 3, 5, 9, 12] # target = 2

# nums = [-1, 0, 3, 5, 9, 12] # target = 12

nums = [-1, 0, 3, 5, 9, 12] # target = -1

print(binary_search(nums, 12))