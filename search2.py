import math

nums = [-1, 0, 2, 3, 5, 9, 12, 29, 34, 43, 44, 59, 63, 65, 70, 71, 74, 80, 81, 88, 92, 95, 100]
target = 92
index_list = []

search = True
# have a loop that repeats for each step
while search:
# an equation that identifies the middle of a list 
    index = math.floor(len(nums) / 2)
    if int(len(nums)) == 1:
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        else:
            print("number doesn't exist")
            print("return -1")
            search = False
    elif int(len(nums)) == 2:
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        elif nums[index] > target:
            nums = nums[:(index):]
        elif nums[index] < target:
            index_list.append(index)
            nums = nums[index::]
    else: 
    # if matched, elif < or > create new list
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        elif nums[index] > target:
            nums = nums[:(index + 1):]
        elif nums[index] < target:
            index_list.append(index)
            nums = nums[index::]