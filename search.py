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
# for illustration purposes, the indexes of each elements are shown on the line below
li = [ 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59 ]
# idx  0  1  2  3  4   5   6   7   8   9   10  11  12  13  14  15  16

super_li = []
for num in range(0, 1000000, 2):
    super_li.append(num)

def binary_search(list, target):
    # keep track of low point -- index
    low = 0
    # keep track of high point -- index
    high = len(list) - 1
    # loop for as long as our low is less than or equal to our high (aka we have a range to search through)
    while low <= high:
        # calculate the middle point -- index
        mid = (low + high) // 2 # // -- forced integer division
        # compare the middle point value to our target
        if list[mid] == target:
            # if equal - return middle
            return mid
        elif list[mid] > target:
            # if middle point is greater - set middle minus one as the new high point
            high = mid - 1
        elif list[mid] < target:
            # if middle point is less - set middle plus one as the new low
            low = mid + 1
    # if the loop ends, then we have searched the enitre list and did not find our target
    return -1

# print(binary_search(li, 2))

def for_loop(list, target):
    # low point
    bot = 0
    # high point
    top = len(list) - 1
    # loop (will not run if given range(higher number, lower number))
    for _ in range(bot, top):
        # calculate mid point
        mid = (bot + top) // 2
        # compare value at mid point to target
        if list[mid] == target:
            # if equal return mid
            return mid
        elif list[mid] > target:
            # if mid greater, set high to mid minus one
            top = mid - 1
        elif list[mid] < target:
            # if mid less, set low to mid plus one
            bot = mid + 1
    # loop ends when there is no longer a range to search for.
    # so if we reach here and have not found our target, it is not present in the list
    return -1

# for num in range(5,1):
#     print(num)

# print(for_loop(li, 29))

# add high and low as paramaters with some default values
def recursion(list, target, high, low = 0):
    # base case (when we have searched through the whole list)
    if low > high:
        return -1
    # calculate middle point
    middle = (low + high) // 2
    # compare middle point value to targer
    if list[middle] == target:
        # if equal - return middle
        return middle
    elif list[middle] > target:
        # if middle is greater, RECURSION run function again and pass in middle minus one as the new high
        return recursion(list, target, middle - 1, low)
    elif list[middle] < target:
        # if middle is less, run function again and pass in middle plus one as new low
        return recursion(list, target, high, middle + 1)
    
# print(recursion(super_li, 999998, len(super_li) - 1))