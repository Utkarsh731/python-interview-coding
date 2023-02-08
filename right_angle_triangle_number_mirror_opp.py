def create_triangle(number_of_rows):
    """
    This function creates a triangle of numbers with the number of rows specified by the input argument.
    If no value is entered for the number of rows, a prompt to enter a number is displayed.
    The triangle is constructed by printing numbers in decreasing order and increasing spaces for each row.

    Parameters:
    number_of_rows (int): The number of rows in the triangle.

    Returns:
    None

    Example:
    create_triangle(5)
    Output:
    12345
     1234
      123
       12
        1

    """
    if not number_of_rows:
        print("Please enter a number")
    else:
        space = 0
        for num in range(number_of_rows, 0, -1):
            print(" "*space, end="")
            for i in range(num):
                print(i+1, end="")
            print()
            space += 1
