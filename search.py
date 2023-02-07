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


def binary_search(list, item):
    # Define high and low
    low = -1
    high = len(list) - 1

    # Create Loop for search
    while low <= high:
        # Define the midpoint of each high and low by taking median
        mid = (low + high) // 2
        # Guess against the item
        check = list[mid]
        # Guess against the item
        if check == item:
            return mid
        # Move according to relation
        if check > item:
            high = mid - 1

        # Move according to relation
        else:
            low = mid + 1
    # If number not in list, return None/False
    return None


list = [-1, 0, 3, 5, 9, 12]
list = [-1, 0, 3, 5, 9, 12]
list = [-1, 0, 3, 5, 9, 12]
list = [-1, 0, 3, 5, 9, 12]
print(binary_search(list, 9))
print(binary_search(list, 2))
print(binary_search(list, 12))
print(binary_search(list, -1))
