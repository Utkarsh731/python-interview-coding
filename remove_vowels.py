'''
Remove all the vowels from a string using decorator
'''

def decorator(remove_vowels):
    def wrapper(*args, **kwargs):
        word = remove_vowels(*args, **kwargs)
        new_word = ''.join(alpha for alpha in word if alpha not in 'aeiouAEIOU')
        return new_word
    return wrapper

@decorator
def remove_vowels(word):
    return word
    
    
print(remove_vowels("rhythdmdivine"))
