# code to find the second max elem in the array

def second_max(arr):
    # check if the length of the array is less than 2
    if len(arr)<2:
        # return error message if the length of the array is less than 2
        return "No second max elem exists"
    # initialize the max_elem with the first element of the array
    max_elem = arr[0]
    # initialize the second_max with a low value
    second_max = -999
    # loop through the array
    for i in range(1, len(arr)):
        # check if arr[i] is greater than max_elem
        if arr[i]>max_elem:
            # set second_max as max_elem
            second_max = max_elem
            # set max_elem as arr[i]
            max_elem = arr[i]
        # check if second_max is less than arr[i]
        elif second_max<arr[i]:
            # set second_max as arr[i]
            second_max = arr[i]
    # return the second_max
    return second_max

# test the function with an array of values
print(second_max([2,1,3 ,455 ,66, 42]))
