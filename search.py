array = [-1, 0, 3, 5, 9, 12]

array2 = [0, 2, 9, 10, 12, 12]
def binarySearch(arr, target, start = 0, end = None):
    if end == None:
        end = len(arr) - 1
    if end < start: 
        print(-1)
        return -1
    # middle = int(((start + end) / 2))
    middle = ((end - start)//2) + start
    # print(end)
    # print(start)
    # print(arr[middle])
    # print(target)
    if arr[middle] == target:
        print(middle)
        # return middle
        return
    elif arr[middle] > target:
        binarySearch(arr, target, start, middle - 1)
    elif arr[middle] < target:
        binarySearch(arr, target, middle + 1, end)
    

    # return arr, target
def binary_search(nums, target):
    low = 0
    high = len(nums)
    middle = high // 2

    while low != middle:
        if nums[middle] == target:
            return middle
        elif target < nums [middle]:
            high = middle
        else:
            low = middle
        distance = high - low
        middle = low + (distance//2)
    return -1

# distance = high - low
# mid = low + (distance / 2)

def otherSearch(arr, target, start = 0, end = None):
    if end == None:
        end = len(arr) - 1
        # print (end)
    if end < start:
        # print (end)
        # print(-1)
        return -1
    # print (end)
    middle = ((end - start)//2) + start
    print(middle)
    if arr[middle] == target:
        print (middle)
        return
    elif arr[middle] < target:
        end =  end - 1
        otherSearch(arr, target, start, end)
    elif arr[middle] > target:
        start += 1
        otherSearch(arr, target, start, end)



print(binary_search(array, 12))
print(binary_search(array, 3))
print(binary_search(array, -1))
print(binary_search(array, 2))

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


