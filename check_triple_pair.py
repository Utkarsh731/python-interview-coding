'''
Given an array A[] of N numbers and another number x,
determine whether or not there exist three elements in A[] whose sum is exactly x.

input =  [1, 4, 45, 6, 10, 8]
sum = 22
output =  "Yes there exists a pair"
'''

def check_pair(arr, total):
    new_arr = set()
    for i in range(0, len(arr)-1):
        remaining_total = total - arr[i]
        for j in range(i+1, len(arr)):
            if remaining_total - arr[j] in new_arr:
                pair = (arr[i], arr[j], remaining_total-arr[j])
                return "Yes there exists a pair"
            new_arr.add(arr[j])
    return "No such pair exists"       



print(check_pair([1, 4, 45, 6, 10, 8], 22))
