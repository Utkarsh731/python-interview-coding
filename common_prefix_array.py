# Given an array of strings, return the common prefixes, if not found return an empty string.
# Ex. ['abcd', 'abb', 'acd'] -> return 'a'

def common_prefix(arr):
    if not len(arr): # check if the array is empty
        return ""
    if len(arr) == 1: # check if the array has only one element
        return arr[0]
    arr.sort() # Sort the array
    first_elem = arr[0] # Get the first element of the array
    last_elem = arr[-1] # Get the last element of the array
    prefix = ""
    for i in range(min(len(first_elem), len(last_elem))):  # Iterate through the smallest length of the first and last element
        if first_elem[i] == last_elem[i]:  # Check if the characters at the current position match
            prefix += first_elem[i]  # If they match, add the character to the prefix
        else:
            break
    return prefix

print(common_prefix(['abcd', 'abb', 'abcd']))  # 'ab'
