'''
Given an array of strings, return the common prefixes, 
if not found return an empty array. Ex. ['abcd', 'abb', 'acd'] -> return 'a'
'''

def common_prefix(arr):
    if not len(arr):
        return ""
    if len(arr) == 1:
        return arr[0]
    arr.sort()
    first_elem = arr[0]
    last_elem = arr[len(arr)-1]
    prefix = ""
    for i in range(0, len(first_elem)):
        if first_elem[i] == last_elem[i]:
            prefix += first_elem[i]
        else:
            break
    return prefix



print(common_prefix(['abcd', 'abb', 'abcd']))
