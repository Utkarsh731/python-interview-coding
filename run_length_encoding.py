'''
Run-length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. This is most efficient on data that contains many such runs, for example, simple graphic images such as icons, line drawings, Conway's Game of Life, and animations. For files that do not have many runs, RLE could increase the file size.
, write a function that returns the Run Length Encoded string for the input string.
For example, if the input string is “aaabbccddd”, then the function should return “3a2b2c3d”
'''

# Define a function for Run-Length Encoding
def run_length_encoding(input_string):
    # Initialize variables to store the previous character and counter
    prev_char = 0
    counter = 0
    # Initialize the output string
    output_string = ""
    # Loop through each character in the input string
    for char in input_string:
        # If the character is the same as the previous character
        if char == prev_char:
            # Increase the counter
            counter += 1
        else:
            # If this is the first character, set the previous character and counter
            if prev_char == 0:
                prev_char = char
                counter = 1
            else:
                # Add the counter and character to the output string
                output_string = output_string + str(counter) + str(prev_char)
                # Reset the previous character and counter
                prev_char = char
                counter = 1
    # Add the last count and character to the output string
    output_string = output_string + str(counter) + str(char)
    # Return the output string
    return output_string

# Call the function and print the result
print(run_length_encoding("aaabbccddd"))

