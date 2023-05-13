import math
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

nums = [-1, 0, 2, 3, 5, 9, 12]
target = 0
# Output should be 4
index_list = []

search = True
# have a loop that repeats for each step
while search:
# an equation that identifies the middle of a list 
    print(f"nums list: {nums}")
    index = math.floor(len(nums) / 2)
    print(f"middle index: {index}")
    if int(len(nums)) == 1:
        # print(f"nums list: {nums}")
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        else:
            print("number doesn't exist")
            print("return -1")
            search = False
    elif int(len(nums)) == 2:
        # print(f"nums list: {nums}")
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        elif nums[index] > target:
            print(f"num: {nums[index]}")
            print("move left in the list")
            print(f"index list: {index_list}")
            nums = nums[:(index):]
        elif nums[index] < target:
            print(f"num: {nums[index]}")
            index_list.append(index)
            print("move right in the list")
            print(f"index list: {index_list}")
            nums = nums[index::]
    else: 
    # if matched, elif < or > create new list
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        elif nums[index] > target:
            print(f"num: {nums[index]}")
            print("move left in the list")
            # index_list.append(index)
            print(f"index list: {index_list}")
            nums = nums[:(index + 1):]
        elif nums[index] < target:
            print(f"num: {nums[index]}")
            index_list.append(index)
            print("move right in the list")
            print(f"index list: {index_list}")
            nums = nums[index::]
        else:
            print("else statement triggered")
            search = False
# repeat unless array length = 1, then it doesn't exist 