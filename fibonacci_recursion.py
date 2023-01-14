# This program prints the fibonacci sequence up to n-th term using recursion

# Function to generate and print the fibonacci sequence
def fibonacci(n):
    # Base case
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Recursive case
        return fibonacci(n-1) + fibonacci(n-2)

# Input from user for number of terms
n = int(input("Enter number of terms: "))

# Loop to print the fibonacci sequence
for i in range(1, n+1):
    print(fibonacci(i))
