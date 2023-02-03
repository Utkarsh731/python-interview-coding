# Define a function to create a triangle
def create_triangle(number_of_rows):
    # Check if the number of rows is not provided or is zero
    if not number_of_rows:
        # If not, print a message to enter a number
        print("Please enter a number")
    else:
        # Loop through the number of rows in reverse order
        for num in range(number_of_rows, 0, -1):
            # Set the number to start from 1
            number = 1
            # Loop to print the number in a row
            for i in range(0, num):
                print(number, end="")
                number += 1
            # Move to the next row
            print()

# Call the function and provide the number of rows as an argument
create_triangle(10)
