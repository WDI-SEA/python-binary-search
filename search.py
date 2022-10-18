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
def BinarySearch(arr, start, mid, end, target):
    if arr[mid] == target:
        return True
    elif (start +1 == end):
        return False 
    else:
        if arr[mid] < target: 
            print("mid less than target ",arr, start , mid , end, target )
            return BinarySearch(arr, mid , int((mid+end)/2) , end, target)
        else:
            print("mid greater than target ",arr, start , mid , end, target )
            return BinarySearch(arr, start, int((start+mid)/2), mid , target)

print(BinarySearch([3,4,7,8,11,12,13,23], 0 , 3, 7, 13))