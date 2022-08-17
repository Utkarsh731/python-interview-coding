'''
Reverse the bits of an 32 bit unsigned integer A
'''

def reverse_bits(num):
    binary_num = bin(num)
    reverse = binary_num[-1:1:-1]
    reverse = reverse + (32 - len(reverse))*'0'
    return int(reverse, 2)


print(reverse_bits(4))
