# Given an array of distinct elements and a number x, find if there is a pair with product equal to x and print all the pairs.

def find_elem(array, x):
    pairs = []  # Initialize an empty list to store pairs
    array.sort()  # Sort the array
    for i in range(0,len(array)-1):  # Iterate through the array
        for j in range(i+1, len(array)):  # Iterate through the array from the next index of i
            if array[i]*array[j]==x:  # Check if the product of the current elements is equal to x
                pair = (array[i], array[j])  # Create a tuple of the current elements
                pairs.append(pair)  # Append the tuple to the pairs list
            elif array[i]*array[j]>x:  # If the product of the current elements is greater than x, break the inner loop
                break
    return pairs  # Return the pairs list

print(find_elem([12,3,2,4,5,6], 24))  # [(2, 12), (3, 8)]
