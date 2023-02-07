
## === ## STATE VARIABLES ## === ##

# range = starts with array[first] --> array[last]
# min = array[first]
# middle = array[middle_index]
# max = array[last]

def binary_search_alg(array, value):
    
    n = len(array)
    # print(n)

    low = 0
    high = n-1
    # print(high)
    guess = int((high+low)/2)
    # print(guess)

    binary_searching = True

    if value < array[low] or value > array[high]:
        print(f'That value doesn\'t exist in this array, so the index is -1')
        return -1

    while binary_searching:

        if (high - low) == 1:
            binary_searching = False
            print(f'That value doesn\'t exist in this array, so the index is -1')
            return -1

        if value == array[guess]:
            binary_searching = False
            print(f'The value you\'re looking for is at index {guess}')
            return guess

        if value > array[guess]:
            print('value > guess')
            # print(low, high, guess)
            low = guess
            high += 1
            guess = int((high+low)/2)
            # print(guess)
            continue

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