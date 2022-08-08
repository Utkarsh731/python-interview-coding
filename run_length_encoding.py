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
                print(char)
                output_string = output_string + str(counter) + str(prev_char)
                prev_char = char
                counter = 1
    output_string = output_string + str(counter) + str(char)
    return output_string

print(run_length_encoding("aaabbccddd"))
