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


def algo(list, target):
    low = 0
    high = len(list)-1
    middle = None
    output = None
    while output != target:
        middle = int(((high + low)/2))
        print(middle)
        if (list[middle] == target):
            output = list[middle]
            print(
                f'Expected output: {target}, Results: {output}, at index: {middle}')
        elif (list[high] == target):
            output = list[high]
            middle = high
            print(
                f'Expected output: {target}, Results: {output}, at index: {middle}')
        elif (list[low] == target):
            output = list[low]
            middle = low
            print(
                f'Expected output: {target}, Results: {output}, at index: {middle}')
        elif (low == middle or high == middle and output != target):
            print(
                f'Expected target: {target} but this does not exist in the list')
            break
        elif (list[middle] > target):
            high = int(middle)
        elif (list[middle] < target):
            low = int(middle)
        elif (list[middle] > target):
            high = int(middle)
        else:
            print(
                f'Low: {low}, high: {high}, middle: {middle}, output: {output}')


# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
nums = [-1, 0, 3, 5, 9, 12]
target = 59

li = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

algo(li, target)
