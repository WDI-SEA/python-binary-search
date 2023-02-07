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

nums = [-1, 0, 3, 5, 9, 12]
nums.sort()

print(nums)

#gives value of index - 12
# print(len(nums)) #index value of length of array - 6
#number to find index of
find_num = 82
#index of middle of array - 3

# print(index_middle)
#middle of the binary array value - 5
# value_array = round(nums[index_middle])
# # middle_num = round(len(nums)/middle_num)
# print(value_array)
end = len(nums) -1
beg = 0
# # print(type(end_array))

# #run this until value of nums = 9
while(beg <= end):
    index_middle = round((end + beg) / 2)
    print("middle index",index_middle)
    if(find_num == nums[index_middle]):
        print(f"The value of {find_num} is at {index_middle}")
        beg = len(nums) + 1
    
    else:
        if(find_num > nums[index_middle]):
            beg = index_middle + 1
            print(f"find num {find_num} is bigger than index {nums[index_middle]}")
        elif(find_num < nums[index_middle]):
            end = index_middle -1
            print(f"find num {find_num} is less than index {nums[index_middle]}")
        

