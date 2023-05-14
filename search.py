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
def search_list(data_list, target):
    first = 0
    last = len(data_list) -1

    while first <= last :
        mid_idx = (first + last) // 2
        if data_list[mid_idx] == target:
            return(f"{target} found at index {mid_idx} ")
        
        if data_list[mid_idx] < target:
            first = mid_idx + 1
            
        if data_list[mid_idx] > target:
            last = mid_idx -1

    return mid_idx

li = [ 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

# print(search_list(li, 17))


def recursion_search(data_list, first, last, target):
    if first > last:
        return f'Could not find {target}'
    
    mid = (first + last) //2
    mid_val = data_list[mid]

    if mid_val == target:
        return print(f"{target} found at index {mid}")
    
    elif mid_val > target:
        last = mid - 1
        return recursion_search(data_list, first, mid -1, target)
    
    elif mid_val < target:
        first = mid + 1
        return recursion_search(data_list, mid + 1, last, target)
    
    
    
print(recursion_search(li, 0, len(li) - 1,29))