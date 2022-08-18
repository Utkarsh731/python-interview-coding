'''
Given a string, check if it is a palindrome by ignoring spaces. E.g. race car would be a palindrome.
'''

def check_palidrome(word):
    word = word.replace(" ","")
    if len(word)%2:
        reverse_word = word[::-1]
        if word == reverse_word:
            return "It is a palindrome"
    return "Not a palindrome"



print(check_palidrome("race car"))
