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

array = [-1, 0, 3, 5, 9, 12]
target = 9

# Binary Search (Iterative)
def binary_search_iterative(array, target):
    # set low and high
    low = 0
    high = len(array) - 1
    # loop until low is greater than high
    while low <= high:
        # find the middle index
        mid = (low + high) // 2
        # if target is found, return the index
        if target == array[mid]:
            return mid
        # if target is less than the middle index, set high to mid - 1
        elif target < array[mid]:
            high = mid - 1
        # if target is greater than the middle index, set low to mid + 1 
        else:
            low = mid + 1
    # if target is not found, return -1
    return -1

    # low = 0
    # high = len(array) - 1
    # while low <= high:
    #     mid = (low + high) // 2
    #     if target == array[mid]:
    #         return True
    #     elif target < array[mid]:
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    # return False

# Binary Search (Recursive)
def binary_search_recursive(array, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            return binary_search_recursive(array, target, low, mid - 1)
        else:
            return binary_search_recursive(array, target, mid + 1, high)
        
    # if low > high:
    #     return False
    # else:
    #     mid = (low + high) // 2
    #     if target == array[mid]:
    #         return True
    #     elif target < array[mid]:
    #         return binary_search_recursive(array, target, low, mid - 1)
    #     else:
    #         return binary_search_recursive(array, target, mid + 1, high)

print(linear_search(array, target))
print(binary_search_iterative(array, target))
print(binary_search_recursive(array, target, 0, len(array) - 1))



