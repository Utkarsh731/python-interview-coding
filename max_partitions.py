def max_partitions(sentence):
    """
    This function takes a sentence as input and returns the maximum number of partitions such that no two substrings have any common character.
    """
    # Initialize dictionary to store ending characters
    ending_charaters = {}
    # Initialize variable to store partition count
    max_partitions = 0
    
    # Iterate through the sentence and store the last index of each character in the dictionary
    for i in range(len(sentence)-1,-1,-1):
        if sentence[i] not in ending_charaters:
            ending_charaters[sentence[i]] = i
    
    # Initialize the ending index as the index of the first character
    ending_index = ending_charaters[sentence[0]]
    
    # Iterate through the sentence and check for partitions
    for i in range(len(sentence)):
        # Check if the current index is less than or equal to the ending index
        if i<=ending_index:
            # Update the ending index if the current character has a higher index
            ending_index = max(ending_index,ending_charaters[sentence[i]])
        else:
            # Increment the partition count
            max_partitions += 1
            # Update the ending index
            ending_index = max(ending_index,ending_charaters[sentence[i]])
            
    # Return the partition count + 1
    return max_partitions+1    


# test case
print(max_partitions('ababcbacadefegdehijhklij'))
