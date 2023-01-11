def create_triangle(number_of_rows):
    if not number_of_rows:
        print("Please enter a number")
    else:
        stars = 1
        for num in range(number_of_rows, 0, -1):
            print(" "*(num-1), end="")
            print("*"*stars)
            stars += 1

create_triangle(5)