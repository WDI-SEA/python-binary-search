
## === ## PSEUDOCODE ## === ##

# input: array[x,y,z], value

# Define beginning variables of min, max, and guess (avg of max/min)

# starting at index of guess, check if value matches.
    # if value > guess:
        # reset min to guess and recalculate guess
    # if value < guess:
        # reset max to guess and recalculate guess
    # if value = guess:
        # stop the loop and return index
    # if value not found:
        # stop the loop and return -1

## === ## STATE VARIABLES ## === ##

# range = starts with array[first] --> array[last]
# min = array[first]
# middle = array[middle_index]
# max = array[last]

def binary_search_alg(array, value):
    
    n = len(array)
    low = 0
    high = n-1
    guess = int((high+low)/2) # average of high and low to check middle of the range

    # to keep the function running in the while loop:
    binary_searching = True

    # to check if the value we're looking for is automatically not found in the array:
    if value < array[low] or value > array[high]:
        print(f'That value doesn\'t exist in this array, so the index is -1')
        return -1

    while binary_searching:

        # if the range is so narrow that low and high are next to each other and guess is still not present:
        if (high - low) == 1:
            binary_searching = False
            print(f'That value doesn\'t exist in this array, so the index is -1')
            return -1

        # if the guess is the value and we've found it in the array:
        if value == array[guess]:
            binary_searching = False
            print(f'The value you\'re looking for is at index {guess}')
            return guess

        # if the value we're looking for is greater than the value at the guess index:
        if value > array[guess]:
            print('value > guess')
            # print(low, high, guess)
            low = guess
            high += 1
            guess = int((high+low)/2)
            # print(guess)
            continue

         # if the value we're looking for is less than the value at the guess index:
        if value < array[guess]:
            print('value < guess')
            high = guess
            guess = int((high+low)/2)
            # print(guess)
            continue

# binary_search_alg([1,2,3,4,6,7,8], 5)

# binary_search_alg([-1, 0, 3, 5, 9, 12],9)

binary_search_alg([-1, 0, 3, 5, 9, 12],2)

# binary_search_alg([-1, 0, 3, 5, 9, 12],12)

# binary_search_alg([-1, 0, 3, 5, 9, 12],-1)

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