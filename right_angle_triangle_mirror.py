def create_triangle(number_of_rows):
    # if the number of rows is not specified, prompt the user to enter a number
    if not number_of_rows:
        print("Please enter a number")
    else:
        # initialize the number of stars to 1
        stars = 1
        # iterate over the range of number of rows
        for num in range(number_of_rows, 0, -1):
            # print the number of spaces on the left, determined by the current iteration number
            print(" "*(num-1), end="")
            # print the number of stars, determined by the current iteration number
            print("*"*stars)
            # increment the number of stars by 1 for the next row
            stars += 1

# call the function with an argument of 5
create_triangle(5)
