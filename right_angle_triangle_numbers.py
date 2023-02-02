def create_triangle(number_of_rows):
    # Check if the number of rows is given or not
    if not number_of_rows:
        print("Please enter a number")
    else:
        # Loop through the number of rows
        for num in range(number_of_rows):
            # Initialize a variable to keep track of the numbers
            number = 1
            # Loop through each row to create the triangle
            for i in range(0, num+1):
                print(number, end="")
                # Increment the number for the next iteration
                number += 1
            # Move to the next line for the next row
            print()

# Call the function to create a triangle with 10 rows
create_triangle(10)
