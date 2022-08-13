'''
Maximize partitions such that no two substrings have any common character
input = '“ababcbacadefegdehijhklij” 
output = 3
'''

def max_partitions(sentence):
    starting_characters = {}
    ending_charaters = {}
    max_partitions = 0
    
    for i in range(len(sentence)-1,-1,-1):
        if sentence[i] not in ending_charaters:
            ending_charaters[sentence[i]] = i
    
    ending_index = ending_charaters[sentence[0]]
    
    for i in range(len(sentence)):
        if i<=ending_index:
            ending_index = max(ending_index,ending_charaters[sentence[i]])
        else:
            max_partitions += 1
            ending_index = max(ending_index,ending_charaters[sentence[i]])
            
    return max_partitions+1    


print(max_partitions('ababcbacadefegdehijhklij'))
