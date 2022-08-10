'''
You are given an array of integers. Return an array of the same size where the element at each index 
is the product of all the elements in the original array except for the element at that index. 
For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24]. You cannot use division in this problem.
'''

def product_array(array):
    output_array = []
    for i in range(0, len(array)):
        num=1
        for x in array:
            if x!=array[i]:
                num=x*num
        output_array.append(num)
    return output_array


print(product_array([1, 2, 3, 4, 5]))
