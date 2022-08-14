'''
Find Square Root of a whole number without using standard functions
'''

def square_root(num):
    i = 2
    if num < 1:
        return "Please enter the number greater than 1"
    if num == 1:
        return 1
    while True:
        match = i*i
        if match == num:
            return i
        elif match > num:
            match = binary_search(num,i-1, i)
            return match
        i += 1


def binary_search(num, i, j):
    middle  = (i+j)/2
    match = middle*middle
    if match == num or abs(match-num)<0.00001:
        return middle
    elif match>num:
        return binary_search(num, i, middle)
    else:
        return binary_search(num, middle, j)

print(square_root(5))
