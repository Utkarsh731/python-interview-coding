def check_palidrome(word):
    """
    This function takes a string as input and checks if it is a palindrome by ignoring spaces.
    """
    # Removing spaces from the input word
    word = word.replace(" ","")
    #Checking if the length of the word is odd
    if len(word)%2:
        # Reversing the word
        reverse_word = word[::-1]
        # Checking if the reversed word is same as the original word
        if word == reverse_word:
            return "It is a palindrome"
    return "Not a palindrome"


# test case
print(check_palidrome("race car"))
