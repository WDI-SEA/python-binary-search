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

    



def binary_search(list, target):
    min = 0
    max = len(list)-1
    mid = 0

    while min <= max:
        mid = (max + min) // 2
        if target == list[mid]:
            return mid

        if target < list[mid]:
            max = mid - 1
        else:
            min = mid + 1
    return -1



result = binary_search([-1, 0, 3, 5, 9, 12], 9)

if result != -1:
    print('found at:', str(result))
else:
    print('not present')















# my 1 hr try. got stuck in infinite loop but decently content with progress.

# def binary_search(list, target):
#     found = False

#     min = 0
#     max = len(list)-1
#     mid = (len(list)-1)//2   
    

#     while found == False:
#         if target == list[mid]:
#             print(mid)
#             found = True
#         elif target < list[mid]:
#             max = mid -1
#             mid = (max - min)//2
#             if target == list[mid]:
#                 print(mid)
#                 found = True
#         else:
#             min = mid + 1
#             mid = (max - min)//2
#             if target == list[mid]:
#                 print(mid)
#                 found = True
                
#         print('yoyo', list, mid)


# binary_search([-1, 0, 3, 5, 9, 12], 0)





 
