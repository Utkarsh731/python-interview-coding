# The function creates a triangle of asterisks with the number of rows specified by the input argument
def create_triangle(number_of_rows):
    # If no value is entered for the number of rows, a prompt to enter a number is displayed
    if not number_of_rows:
        print("Please enter a number")
    else:
        # Initialize the variable 'space' to keep track of the number of spaces to be printed before each row of asterisks
        space = 0
        # A for loop is used to create the triangle by printing asterisks in decreasing order and increasing spaces for each row
        for num in range(number_of_rows, 0, -1):
            print(" "*space, end="") # print spaces before each row
            print("*"*num) # print asterisks for each row
            space += 1 # increase the number of spaces for the next row

# Call the function and pass an argument of 5
create_triangle(5)
