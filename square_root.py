# Find Square Root of a whole number without using standard functions

def square_root(num):
    # initialize variable i with value 2
    i = 2
    # check if the input number is less than 1
    if num < 1:
        # return error message if the number is less than 1
        return "Please enter the number greater than 1"
    # check if the input number is equal to 1
    if num == 1:
        # return 1 if the input number is equal to 1
        return 1
    # infinite loop
    while True:
        # calculate the square of i
        match = i*i
        # check if match is equal to the input number
        if match == num:
            # return i if match is equal to the input number
            return i
        # check if match is greater than the input number
        elif match > num:
            # call the binary_search function with input parameters num, i-1, i
            match = binary_search(num,i-1, i)
            # return the result of binary_search function
            return match
        # increment the value of i by 1
        i += 1

def binary_search(num, i, j):
    # calculate the middle value of i and j
    middle  = (i+j)/2
    # calculate the square of middle value
    match = middle*middle
    # check if match is equal to num or the absolute difference between match and num is less than 0.00001
    if match == num or abs(match-num)<0.00001:
        # return middle if the above condition is met
        return middle
    # check if match is greater than num
    elif match>num:
        # call binary_search function with input parameters num, i, middle
        return binary_search(num, i, middle)
    # if match is not equal to num and not greater than num
    else:
        # call binary_search function with input parameters num, middle, j
        return binary_search(num, middle, j)

# print the square root of 5
print(square_root(5))
