# The function creates a triangle of asterisks with the number of rows specified by the input argument
def create_triangle(number_of_rows):
    # If no value is entered for the number of rows, a prompt to enter a number is displayed
    if not number_of_rows:
        print("Please enter a number")
    else:
        # A for loop is used to create the triangle by printing asterisks in increasing order for each row
        for num in range(number_of_rows):
            print("*"*(num+1))

# Call the function and pass an argument of 10
create_triangle(10)
