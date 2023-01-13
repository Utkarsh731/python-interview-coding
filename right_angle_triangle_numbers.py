def create_triangle(number_of_rows):
    if not number_of_rows:
        print("Please enter a number")
    else:
        for num in range(number_of_rows):
            number = 1
            for i in range(0, num+1):
                print(number, end="")
                number += 1
            print()

create_triangle(10)