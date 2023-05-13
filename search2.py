import math

nums = [-1, 0, 2, 3, 5, 9, 12, 29, 34, 43, 44, 59, 63, 65, 70, 71, 74, 80, 81, 88, 92, 95, 100]
target = 63
index_list = []

search = True
# have a loop that repeats for each step
while search:
    # an equation that identifies the middle index of a list 
    index = math.floor(len(nums) / 2)
    # if the lenght of the list == 1, unique instructions because it's either the target number or the number doesn't exist
    if int(len(nums)) == 1:
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        else:
            print("number doesn't exist")
            print("return -1")
            search = False
    else: 
    # if matched, elif < or > create new list
        if nums[index] == target:
            output = sum(index_list) + index
            print(f"{target} is found at index {output}")
            search = False
        elif nums[index] > target:
            nums = nums[:index:]
        elif nums[index] < target:
            index_list.append(index)
            nums = nums[index::]