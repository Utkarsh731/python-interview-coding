def decorator(remove_vowels):
    """
    This function takes a function as input and return a wrapper function
    """
    def wrapper(*args, **kwargs):
        # calling the input function
        word = remove_vowels(*args, **kwargs)
        # Removing vowels from the returned string using list comprehension
        new_word = ''.join(alpha for alpha in word if alpha not in 'aeiouAEIOU')
        return new_word
    return wrapper

# decorator function
@decorator
def remove_vowels(word):
    return word

#test case
print(remove_vowels("rhythdmdivine"))
