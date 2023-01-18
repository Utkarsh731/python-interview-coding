from collections.abc import Iterable

def flatten(input_array, output_array):
    """
    This function takes an array consisting of many inner arrays and flattens it into a single array.
    """
    #Iterate over each element in the input array
    for array in input_array:
        #Check if the element is a list
        if type(array) == list:
            #If it is a list, recursively call the flatten function
            flatten(array, output_array)
        else:
            #If it is not a list, append the element to the output array
            output_array.append(array)
    return output_array



def flatten_list(lst):
    """
    This function takes an n-dimensional list and flattens it into a one-dimensional list.
    """
    flat_list = []
    for item in lst:
        if isinstance(item, Iterable) and not isinstance(item, str):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

#test case
print(flatten_list([[6,4,7,[9,5,4,[2,4,8]]],[2,2,7],[9,0,7,[9,3,1,8,5]]]))

#test case
print(flatten([[6,4,7,[9,5,4,[2,4,8]]],[2,2,7],[9,0,7,[9,3,1,8,5]]],[]))

