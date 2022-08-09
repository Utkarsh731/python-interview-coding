'''
Given a string ‘str’ of digits and an integer ‘n’,
build the lowest possible number by removing ‘n’ digits from the string and not changing the order of input digits.
str = "4325043" , n=3
output = "2043"
'''

def lowest_possible_num(string, n):
    new_stack = []
    for i in string:
        if not new_stack:
            new_stack.append(i)
        else:
            current = int(i)
            previous = int(new_stack[len(new_stack)-1]) 
            if current<previous and n>0:
                new_stack.pop()
                new_stack.append(i)
                n=n-1
            else:
                new_stack.append(i)
    return ''.join(new_stack)
        

print(lowest_possible_num("765028321",5))
