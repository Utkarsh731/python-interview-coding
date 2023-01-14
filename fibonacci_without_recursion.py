# This program prints the fibonacci sequence up to n-th term

# Function to generate and print the fibonacci sequence
def fibonacci(n):
   # Initializing first two terms
   a = 0
   b = 1
   print(a)
   print(b)
   # Looping through to generate and print next terms
   for i in range(2,n):
       c = a + b
       print(c)
       a = b
       b = c

# Input from user for number of terms
n = int(input("Enter number of terms: "))

# Check if input is valid
if n <= 0:
   print("Please enter a positive integer")
else:
   fibonacci(n)
