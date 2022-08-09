'''
Given an array consisting many inner arrays, 
flatten the array into one: example: input:
[[6,4,7,[9,5,4,[2,4,8]]],[2,2,7],[9,0,7,[9,3,1,8,5]]] 
output: [6,4,7,9,5,4,2,4,8,2,2,7,9,0,7,9,3,1,8,5]
'''


def flatten(input_array, output_array):
    for array in input_array:
        if type(array) == list:
            flatten(array, output_array)
        else:
            output_array.append(array)
    return output_array
    

print(flatten([[6,4,7,[9,5,4,[2,4,8]]],[2,2,7],[9,0,7,[9,3,1,8,5]]] , []))
        
            
        
