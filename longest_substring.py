# Given a string S consisting only of opening and closing parenthesis 'ie '(' and ')', 
# find out the length of the longest valid(well-formed) parentheses substring.
# NOTE: Length of the smallest valid substring ( ) is 2.

def longest_substring(word):
    stack = [] # initialize an empty stack
    max_len = 0 # initialize max_len as 0
    for char in word: # iterate through the string
        if char == "(": # if the current character is an open parenthesis
            stack.append("(") # append it to the stack
        else:
            if len(stack): # if the stack is not empty
                stack.pop() # remove the last open parenthesis from the stack
                max_len += 2 # increase the max_len by 2
    return max_len

print(longest_substring('()(()))))'))  # 4
