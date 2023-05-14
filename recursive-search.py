''''
MATHEMATICS•LINGUISTICS
relating to or involving the repeated application of a rule, definition, or procedure to successive results.
"this restriction ensures that the grammar is recursive"
COMPUTING
relating to or involving a program or routine of which a part requires the application of the whole, so that its explicit interpretation requires in general many successive executions.
"a recursive subroutine"
'''
# Example 4:
# Input: nums = [-1, 0, 3, 5, 9, 12], target = -1
# Output: 0
# Explanation: -1 exists in the list and its index is 0

def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
    # find the middle index
    mid_idx = int(len(arr) / 2)
    # check if mid index equals target
    middle = arr[mid_idx]

    if middle == target:
        return mid_idx
    elif middle > target:
        # check idx 0 - mid_idx
        return recursive_binary_search(arr[:mid_idx], target)
    else:
        # check mid_idx + 1 - last idx
        result = recursive_binary_search(arr[mid_idx + 1:], target)
        if result == -1:
            return -1
        else:
            return result + mid_idx + 1

print(recursive_binary_search([-1, 0, 3, 5, 9, 12], 5))