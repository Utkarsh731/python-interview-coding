'''
Given a matrix where each row and each column is sorted, check whether the given number is present in the matrix.
'''

def find_num_matrix(matrix, num, length):
    i=0
    j=length-1
    while(i<length and j>0):
        if matrix[i][j]==num:
            return "Number found at "+str(i) +" "+str(j)
        elif matrix[i][j]>num:
            j -= 1
        else:
            i +=1
    return "Number not found"


print(find_num_matrix(matrix=[ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ], num=29, length=4))
