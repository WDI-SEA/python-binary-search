# def sumArrayOfNums(arr, index = 0, sum = 0):
#     if(index == len(arr)):
#         return sum
#     sum += arr[index]
#     print(f'Adding {sum} + {arr[index]} ')
#     return sumArrayOfNums(arr, index+1, sum)

list = [2,4,5,8]
# print(sumArrayOfNums(list))

def sumArrayOfNums(arr, index = 0, sum = 0):
    def rSum():
        if(index == len(arr)):
            return sum
        sum += arr[index]
        index + 1
        return rSum()
    return rSum()

print(sumArrayOfNums(list))