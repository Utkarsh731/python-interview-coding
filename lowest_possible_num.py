def lowest_possible_num(string, n):
    """
    This function takes a string of digits and an integer n, and returns the lowest possible number by removing n digits from the string and not changing the order of input digits.
    """
    new_stack = []
    #Iterate over each digit in the string
    for i in string:
        #Check if the stack is empty
        if not new_stack:
            new_stack.append(i)
        else:
            current = int(i)
            previous = int(new_stack[len(new_stack)-1])
            #If the current digit is smaller than the previous one and n>0, remove the previous one and append the current one
            if current<previous and n>0:
                new_stack.pop()
                new_stack.append(i)
                n=n-1
            else:
                new_stack.append(i)
    #Join the stack elements to form the string
    return ''.join(new_stack)


#test case
print(lowest_possible_num("765028321",5))
