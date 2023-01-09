def create_triangle(number_of_rows):
    if not number_of_rows:
        print("Please enter a number")
    else:
        for num in range(number_of_rows, 0, -1):
            print("*"*(num+1))

create_triangle(10)