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

def search(nums, target):
    # assume the entire list is our range for starters
    low = 0
    high = len(nums)
    mid = high // 2
    # edge cases if the target is first or last in the list
    if nums[low] == target:
        return low
    if nums[high - 1] == target:
        return high - 1
    # loop until we explicitly break
    while True:
        # we have found the target!
        if nums[mid] == target:
            return mid
        # if we are moving down
        elif nums[mid] > target:
            # move high down to current mid, recalc mid
            high = mid
            mid = high // 2
        # if we are moving up
        elif nums[mid] < target:
            # move low up to mid, recalc mid
            low = mid
            # need to know the difference between high and new low
            diff = high - low
            # find the mid point of the diff, add to low to get new mid
            mid = low + (diff // 2)

        # if we are out of bounds -- need to break loop and return -1
        if mid == low or mid == high:
            return -1
        if low >= high or high <= low:
            return -1

nums = [-1, 0, 3, 5, 9, 12]

print('MVP')

print(search(nums, 9))
print(search(nums, 2))
print(search(nums, 30))
print(search(nums, 12))
print(search(nums, -1))

# bonus
def search_recursive(nums, target, **kwargs):
    # on first recursion set high an low
    high = kwargs.get('high', len(nums) - 1)
    low = kwargs.get('low', 0)
    mid = ((high - low) // 2) + low 

    # base cases -- if we found target
    if nums[high] == target:
        return high
    elif nums[low] == target:
        return low
    elif nums[mid] == target:
        return mid
    # or if we are out of bounds
    elif mid == low or mid == high:
        return -1
    
    # recursive cases:
    if nums[mid] > target:
        # move down
        return search_recursive(nums, target, low=low, high=mid)
    elif nums[mid] < target:
        # move up
        return search_recursive(nums, target, low=mid, high=high)

print('BONUS')

print(search_recursive(nums, 9))
print(search_recursive(nums, 2))
print(search_recursive(nums, 30))
print(search_recursive(nums, 12))
print(search_recursive(nums, -1))
