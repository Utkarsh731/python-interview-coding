def longest_substring(word: str) -> int:
    """
    Calculates the length of the longest valid parentheses substring in a given string.

    Parameters:
        word (str): A string consisting only of '(' and ')'.

    Returns:
        int: The length of the longest valid parentheses substring.

    Example:
        >>> longest_substring('()(()))))')
        4
    """
    stack = [-1]  # stack to store indices
    max_length = 0

    for i, char in enumerate(word):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length
