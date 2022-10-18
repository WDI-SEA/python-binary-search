"""
Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
"""
Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
"""
Example 3:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 12
Output: 5
Explanation: 12 exists in the list and its index is 5
"""
"""
Example 4:
Input: nums = [-1, 0, 3, 5, 9, 12], target = -1
Output: 0
Explanation: -1 exists in the list and its index is 0
"""
# psuedo code:
"""
binary_search = (array, targetValue)

let min = 0 and max = n-1
    min = 0
    max = array.length -1

if max < min target isnt present
    if(max < min)
        return f"the {target.value} does not exist in this array"

compute guess as avg of min and max rounded down to integer
if array[guess] = target: stop, return guess
    if(array[i] === targetValue)
        return
else if array[guess] <target set max = guess + 1
    elif (array[i] < target)
    max = guess +1
else set max = guess -1
    else
    max = guess + 1
go back to step 2

"""

def binary_search(array, targetValue):
    min = 0
    max = len(array) -1

    while(min < max):
        mid = int((min + max) /2)

        if(array[mid] == targetValue):
            return f"the number is {mid}"
        elif(targetValue < array[mid]) :
            max = mid -1
        elif(targetValue > array[mid]):
            min = mid +1

    return -1

# print(binary_search([-1, 0, 3, 5, 9, 12],9))
# print(binary_search([-1, 0, 3, 5, 9, 12],2))


# -------------------------------- REVIEW ANSWERS ----------------------------------------------
def search(nums, target):
# keep track of the range
    # high index
    high = len(nums)
    # mid --comparison index - forced integer division rounds down same as math.floor
    mid = high //2
    # low index
    low = 0
# might need edge case for first and last values in the list
    if nums[low] == target:
        return low
    # loop until  conditions are met : either found the target or determined target isnt in the array 
    while True:
        # check id mid == target -> 
        if nums[mid] == target:
            # return index of mid
            return mid
        # if mid < target
        elif nums[mid] < target:
            # move the window to the right -> this makes the new low point the mid
            low = mid
            # recalc the new mid and restart loop
        # if mid > target
        else:
            #  move window to the left makes the mid the new high
            high = mid
            # recalc new mid and restart loop
        
        # recalc new mid
        distance = high - low 
        mid = low + (distance //2 )

        print(f'high: {high} mid:{mid} low:{low}')

         # else if target not in array
        if low == mid:
            return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print("it should be four", search(nums, target))

   



    
    
