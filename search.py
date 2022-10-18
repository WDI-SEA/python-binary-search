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

# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
 
# ! First attempt
#TODO step 1: Find the length of the array
# def findNum(target):
#TODO Step 2: find the middle point betweent array[0] and the final index of the array
    # high = len(nums)
    # low = nums[0]
    # mid = high / 2
#TODO Step 3: check if the middle point to see if it is < then the target or > than the targer
    # if mid > target:
    #     high = mid
    #     low = nums[0]
    #     mid = int(high / 2)
#TODO Step4: If the middle is >  set the middle as the new end point and keep the array[0] as the low repeat step 2 and 3
    # if mid < target:
    #     low = mid
    #     mid = high - low 
#TODO Step5: if the middle is < than the middle point. set the middle as the low point and keep the high point. repeat steps 2 and 3
    # if mid == target:
    #     print('YES', mid, target)
#TODO step6: repeat steps 4 and 5 until the middle point is = to the target aka if x == T return TRUE

# findNum()


# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
# high = len(nums)  - 1
# low = nums[0]
# mid = high / 2


# ? testing making sure the numbers are correct.
# def find_target():
#     if mid < target:
#         low = int(mid)
        
#         print(low, high)

# find_target()

#! Attempt 2 before more research / I was actually closer than I realized!
# def find_the_index(list,i):
#     while  low < high:
#         mid = (high + low) // 2
#         if list[mid] < i:
#             low = mid 
#         elif list[mid] > i:
#             high = mid 
#         else:
#             return mid 
#     

# answer = find_the_index(nums,target)
# print(str(answer))


#! Accidently saw the answer: 

def search(list, n):
    #! Differences in my code vs code online ->  I had my variables declared outside of the function. 
    #! I did not have -1 / +1 in my if statments or on line 88, but it makes sense because the array position starts at [0] and not [1]
    low = 0
    high = len(list) -1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        
        if list[mid] < n:
            low = mid + 1
        elif list[mid] > n:
            high = mid - 1
        else:
            return mid
    #! I did not have this return in my attempts, still unsure of how exactly this works, but I do understand the -1 is returned if the target (n) is not found in the list
    return - 1

nums = [-1, 0, 3, 5, 9, 12]
target = -1

result = search(nums,target)

#! did not have this if statement in my code but I understand that if the function does not return -1 print the result and if it does print it was not found.
if result != -1:
    print('Answer ->', str(result))
else:
    print('Not found in search')