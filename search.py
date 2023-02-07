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

# Time Complexity: O(n)  -- refers to the amount of time an algorithm takes to run as a function of the size input. It is usually expressed using big O notation. The big O notation describes the worst-case scenario, and can be used to describe the execution time required or the space used by an algorithm. `O(n)` is the complexity of an algorithm that takes proportional to the size of the input `n`

# O(n): use this notation when the running time of your algorithm grows linearly with the size of the input, such as in linear search or simple sorting algorithms.
# O(log n): Use this notation when the running time of your algorithm grows logarithmically with the size of the input, such as in binary search or algorithms that use divide-and-conquer techniques like merge sort or quick sort.
# O(n^2): Use this notation when the running time of your algorithm grows quadratically with the size of the input, such as in bubble sort or selection sort.

# Space Complexity: O(1) -- refers to the amount of memory used by an algorithm during execution. `O(1)` is the space complexity of an algorithm that uses a constant amount of memory, independent of the size of the input.

# recap - linear search searches for the solution by checking each element in the list. It is the simplest search algorithm. It is also the slowest search algorithm. It is O(n) time complexity and O(1) space complexity.
# binary search finds the position of a target by repeatedly dividing the search interval in half. It is the fastest search algorithm. It is O(log n) time complexity and O(1) space complexity.

# O(log n) is much faster than O(n)
# O(log n) is much faster than O(n^2)



# # LINEAR SEARCH
# def search(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#         return -1

# BINARY SEARCH
def search(nums, target):
        # defining the left and right pointers. left is starting at the beginning of the list and right is starting at the end of the list
    left = 0
    right = len(nums) - 1
        # using a while loop to check if the left pointer is less than or equal to the right pointer
    while left <= right:
        # defining mid as the middle of the list. using floor division to round down to the nearest whole number in case the list has an odd number of elements. using the left and right pointers to find the middle of the list
        mid = left + (right - left) // 2
        # if the middle of the list is equal to the target, return the index of the middle of the list.
        if nums[mid] == target:
            return mid
            # if the middle of the list is less than the target, move the left pointer to the right by one.
        elif nums[mid] < target:
            left = mid + 1
            # if the middle of the list is greater than the target, move the right pointer to the left by one. if the target is not found, return -1
        else:
            right = mid - 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))

