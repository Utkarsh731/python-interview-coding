# Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.

def check_pair(arr, total):
    seen = set() # initialize an empty set to store elements
    for i in range(len(arr)):
        remaining_total = total - arr[i] # calculate the remaining total
        for j in range(i+1, len(arr)):
            if remaining_total - arr[j] in seen:  # check if the complement exists in the set
                return "Yes there exists a pair"  # return yes if exists
            seen.add(arr[j]) # add the current element to the set
    return "No such pair exists" # return no if no such pair exists

print(check_pair([1, 4, 45, 6, 10, 8], 22))  # Yes there exists a pair
