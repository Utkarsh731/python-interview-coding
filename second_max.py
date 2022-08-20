'''
write the code to find the second max elem in the array
'''

def second_max(arr):
    if len(arr)<2:
        return "No second max elem exists"
    max_elem = arr[0]
    second_max = -999
    for i in range(1, len(arr)):
        if arr[i]>max_elem:
            second_max = max_elem
            max_elem = arr[i]
        elif second_max<arr[i]:
            second_max = arr[i]
    return second_max

print(second_max([2,1,3 ,455 ,66, 42]))
