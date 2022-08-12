'''
Check if the string contains balance parenthesis or not
'''

def balance_parentheses_solution_one(input_string):
    open_brackets = '{[('
    bracket_stack = list()
    for val in input_string:
        if val in open_brackets:
            bracket_stack.append(val)
        else:
            if len(bracket_stack):
                elem = bracket_stack[-1] 
                if (elem == "{" and val == "}") or (elem == "[" and val == "]") or (elem == "(" and val == ")") :
                    bracket_stack.pop()
                else:
                    return "Not balanced"
            else:
                return "Not balanced"
    if bracket_stack:
        return "Not balanced"
    return "Balanced"
    

def balance_parentheses_solution_two(input_string):
    open_brackets = '{[('
    closed_brackets = '}])'
    bracket_stack = list()
    for val in input_string:
        if val in open_brackets:
            bracket_stack.append(val)
        else:
            if len(bracket_stack):
                elem = bracket_stack[-1]
                open_index = open_brackets.index(elem)
                close_index = closed_brackets.index(val)
                if close_index == open_index :
                    bracket_stack.pop()
                else:
                    return "Not balanced"
            else:
                return "Not balanced"
    if bracket_stack:
        return "Not balanced"
    return "Balanced"

print(balance_parentheses_solution_two("[{}{}]"))
