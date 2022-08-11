'''
Find if Given number is power of 2 or not. More specifically, find if given number can be expressed as 2^k where k >= 1.
'''



def power_of_two_sol_one(num):
    for i in range(0,1000):
        if 2**i == num:
            return "Yes, number can be expressed as 2^k"
        elif 2*i > num:
            return "No, number cannot be expressed as 2^k"
 
 
def power_of_two_sol_two(num):
    if (num & (num-1))==0:
        return "Yes, number can be expressed as 2^k"
    else:
        return "No, number cannot be expressed as 2^k"

 

