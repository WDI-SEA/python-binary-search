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
# ##### RECURSIVE 
# function named binary_search that takes parameters of arr, low, high, x
    # x is value to be searched within the array of arr
def binary_search(arr, low, high, x):
    # check the to see if upper bound is greater than or equal to lower bound. if true, target value may be present in array and search should continue
    if high >= low: 
        # calculates midpoint of array. // operator is floor division operation in PieThon, which rounds result down to nearest integer
        mid = (high + low)// 2

        # checks if the element at the midpont of the array is equal to the target value. If true, target value has been found and function returns index position of target value
        if arr[mid] == x:
            return mid
        
        # checks if value in the middle of the array is greater than target value. If true, it means target value can only be to the left half of the array and to continue the search in the left half
        elif arr[mid] > x:
            # calling the function but setting the upper bound to one less than the current midpoint and the lower bound remaining the same
            return binary_search(arr, low, mid - 1, x)
        
        # else the element can only be present in the right subarray; if the element at the midpoint of the array is less than the target value, the target value can only be present in the right half of the array
        else: 
            # calling the function but setting the lower and upper bounds set to the right of the midpoint.
            return binary_search(arr, mid + 1, high, x)
    
    else: 
        # if the upper bound is not greater than or equal to the lower bound element is not present in the array; function returns value of -1 
        return -1

### ITERATIVE
# def binary_search(arr, x):
#     # starting index of array
#     low = 0
#     # ending index of the array, sets initial value of upper index bound of the search space to the index of the last element in the array
#     high = len(arr) -1 
#     # sets mid point to 0
#     mid = 0

#     while low <= high: 
#         mid = (high + low) // 2 

#         if arr[mid] < x: 
#             low = mid + 1

#         elif arr[mid] > x:
#             high = mid - 1
        
#         else:
#             return mid
#     return -1 

arr = [-1, 0, 3, 5, 9, 12]
prompt = ""
print('Enter input here: ')
x = input(prompt)

#convert x value to number
x = int(x) 

# len returns number of elements in a collection
# 0 = starting index of array, lower bound of the array, len(arr) - 1 is upper bound of array
result = binary_search(arr, 0, len(arr) -1, x) 

print(f'Target is {x} and the array index position is: {result}')
