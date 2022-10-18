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

print(binary_search([-1, 0, 3, 5, 9, 12],9))



    
    
