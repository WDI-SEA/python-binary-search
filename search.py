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
nums = [-1, 0, 3, 5, 9, 12]
target = 2
# target = 12
# target = -1


def binary_search():
    window = nums
    window_low = 0
    window_high = int(len(window)-1)
    middle = int(window_high/2)
    searching = True 
    # Set a while loop to continue searching until the target is found
    while (searching == True):
        if (window_high -1 == window_low):
            if (target == window[window_high]):
                searching = False
                print(window_high)
            elif (target == window[window_low]):
                searching = False
                print(window_low)
            else:
                searching = False
                print("Target does not exist in nums, index -1")
        # Check if the target is equal to the middle of the window
        elif (target ==  window[middle]):
            # return the index where the target was found
            print(f"found {target} at index {middle}")
            # turn off the while loop
            searching = False
        # Check if the the target is greater than the middle of the window
        elif (target > window[middle]):
            # Move the bottom of the window to the middle
            window_low = middle
            # Move the middle point to half way between the high and the new low
            middle = window_low + int((window_high - window_low)/2)
            print(f"High {window_high}, Low {window_low}, Middle {middle}")
        # Check if the target is less than the middle of the windo
        elif (target < window[middle]):
            # Move the top of the window to the middle
            window_high = middle
            # Move the middle to half way between the new high and the low
            middle = window_high - int((window_high - window_low)/2)
            print(f"High {window_high}, Low {window_low}, Middle {middle}")

# print(binary_search())

# RECURSIVE refactor

def binary_search_recursive(list, target, window_low, window_high, middle):
    # Check if the target is equal to the middle of the window
    if (window_high < window_low):
        print(f"Target of {target} does not exist in this list")  
    elif (target == list[middle]):
        print(f"found {target} at index {middle}")
    elif(target > list[middle]):
        window_low = middle + 1
        middle = window_low + int((window_high - window_low)/2)
        print(f"High {window_high}, Low {window_low}, Middle {middle}")
        binary_search_recursive(list, target, window_low, window_high, middle)
    elif(target < list[middle]):
        window_high = middle - 1
        middle = window_low + int((window_high - window_low)/2)
        print(f"High {window_high}, Low {window_low}, Middle {middle}")
        binary_search_recursive(list, target, window_low, window_high, middle)
    else:
        print(f"High {window_high}, Low {window_low}, Middle {middle}")


# binary_search()
binary_search_recursive(nums, target, 0, int(len(nums)-1), int(((len(nums)-1)/2)))