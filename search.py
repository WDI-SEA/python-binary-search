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

def solve(arr,find):
    upper = len(arr)
    lower = 0
    # divides by 2 and floors to find mid
    mid = upper//2
    found = False
    # first check for the lower boundary
    if arr[lower] == find:
        print(lower)
        return lower
    while found != True:
        # check if the middle of the search is equal to the target
        if arr[mid] == find:
            found = True
            print(mid)
            return mid
            # updatind region of array to look over
        elif arr[mid] < find:
            lower = mid
        else:
            # updating region of array to look over
            upper = mid

        # updating mid dependent on the elif and else from above
        mid = ((upper-lower)//2)+ lower

        # if mid is equal to lower that means we searched through the designated area and couldn't find it in the array so it does not exist
        if mid == lower:
            print('not found in array')
            return -1

solve([-1, 0, 3, 5, 9, 12],12)