'''
Write a code to print the diamond shape:
input =4
output =
   *
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   *

'''
# This code prints a diamond shape of n rows
n = int(input("Enter the number of rows: "))
c = n - 1

# Upper half of the diamond
for i in range(1, n + 1):
    # Print spaces to align the shape
    print(" " * c, end="")
    c -= 1
    # Print stars to form the shape
    for j in range(0, i):
        print("*", end=" ")
    print()

# Lower half of the diamond
for i in range(0, n):
    # Print spaces to align the shape
    print(" " * i, end="")
    # Print stars to form the shape
    for j in range(i, n):
        print("*", end=" ")
    print()
