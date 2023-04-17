# map
#you have a list of integers and you want to double each one:
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)
#convert a list of strings to integers
strings = ["1", "2", "3", "4", "5"]
numbers = list(map(int, strings))
print(numbers)

#filter
#list of numbers and you want to filter out the even ones:
numbers = [1, 2, 3, 4, 5]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)
# remove empty strings from a list:
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: len(x) > 0, strings))
print(non_empty)

#reduce

from functools import reduce
#list of numbers and you want to calculate their sum :
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
#find the maximum value in a list
numbers = [1, 7, 3, 9, 5]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
