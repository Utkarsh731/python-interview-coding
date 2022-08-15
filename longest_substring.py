'''
Given a string S consisting only of opening and closing parenthesis 'ie '(' and ')', 
find out the length of the longest valid(well-formed) parentheses substring.
NOTE: Length of the smallest valid substring ( ) is 2.
'''

def longest_substring(word):
    stack = []
    max_len = 0
    for word in word:
        if word == "(":
            stack.append("(")
        else:
            if len(stack):
                stack.pop()
                max_len += 2
    return max_len


print(longest_substring('()(()))))'))
