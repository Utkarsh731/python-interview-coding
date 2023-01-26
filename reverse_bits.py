def reverse_bits(num):
    """
    This function takes in an unsigned 32-bit integer, num, and reverses its bits. It returns the reversed bit version of the input integer
    :param num: 32-bit unsigned integer
    :return: reversed bit version of the input integer
    """
    binary_num = bin(num) #convert the integer to its binary representation
    reverse = binary_num[-1:1:-1] #reverse the order of the bits in the binary string
    reverse = reverse + (32 - len(reverse))*'0' #pad the reversed binary string with zeroes to make it 32 bits
    return int(reverse, 2) #convert the binary string back to an integer and return

print(reverse_bits(4))
