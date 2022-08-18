'''
You have an array of n elements, and a sum. Check if any 2 elements in the array sum to the given sum.
input = [0, -1, 2, -3, 1]
sum = -2
output = (-3, 1)
'''

def check_pair(arr, total):
    output = []
    new_arr = []
    for i in arr:
        if (total - i) in new_arr:
            pair = (i, total-i)
            output.append(pair)
        new_arr.append(i)
    return output



print(check_pair([1, 4, 45, 6, 10, 8], 16))
