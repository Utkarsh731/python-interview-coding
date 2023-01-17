# Given a matrix where each row and each column is sorted, check whether the given number is present in the matrix.

def find_num_matrix(matrix, num, length):
    i = 0 # Initialize i as row index
    j = length-1 # Initialize j as column index
    while i < length and j >= 0:
        if matrix[i][j] == num: # Check if the current element is the given number
            return "Number found at "+str(i) +" "+str(j) # Return the position of the number if found
        elif matrix[i][j] > num: # If the current element is greater than the given number
            j -= 1 # Move to the left column
        else:
            i += 1 # Move to the next row
    return "Number not found" # Return this if the number is not found

print(find_num_matrix(matrix=[ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ], num=29, length=4))  # Number found at 2 1
