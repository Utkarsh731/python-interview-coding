'''
Run-length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. This is most efficient on data that contains many such runs, for example, simple graphic images such as icons, line drawings, Conway's Game of Life, and animations. For files that do not have many runs, RLE could increase the file size.
, write a function that returns the Run Length Encoded string for the input string.
For example, if the input string is “aaabbccddd”, then the function should return “3a2b2c3d”
'''

def run_length_encoding(input_string):
    prev_char = 0
    counter = 0
    output_string = ""
    for char in input_string:
        if char == prev_char:
            counter += 1
        else:
            if prev_char == 0:
                prev_char = char
                counter = 1
            else:
                output_string = output_string + str(counter) + str(prev_char)
                prev_char = char
                counter = 1
    output_string = output_string + str(counter) + str(char)
    return output_string

print(run_length_encoding("aaabbccddd"))
