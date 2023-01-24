def product_array(array):
    """
    This function takes an array of integers and returns an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.
    """
    output_array = []
    #iterating through the array
    for i in range(0, len(array)):
        num=1
        #calculating the product of all elements except the current element
        for x in array:
            if x!=array[i]:
                num=x*num
        #append the product to the output array
        output_array.append(num)
    return output_array


#test case
print(product_array([1, 2, 3, 4, 5]))
