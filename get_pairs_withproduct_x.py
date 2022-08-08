'''
Given an array of distinct elements and a number x, find if there is a pair with product equal to x.
and print all the pairs
'''

def find_elem(array, x):
    pairs = []
    array.sort()
    for i in range(0,len(array)-1):
        for j in range(i+1, len(array)):
            if array[i]*array[j]==x:
                pair = (array[i], array[j])
                pairs.append(pair)
                break
            elif array[i]*array[j]>x:
                break
    return pairs


print(find_elem([12,3,2,4,5,6], 24))
