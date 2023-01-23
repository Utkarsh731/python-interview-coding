def power_of_two_sol_one(num):
    """
    This function takes an integer as input and checks if it can be expressed as 2^k where k >= 1.
    """
    # Iterating through all possible values of k from 0 to 1000
    for i in range(0,1000):
        # Checking if 2^i is equal to the given number
        if 2**i == num:
            return "Yes, number can be expressed as 2^k"
        # Checking if 2^i is greater than the given number
        elif 2*i > num:
            return "No, number cannot be expressed as 2^k"


def power_of_two_sol_two(num):
    """
    This function takes an integer as input and checks if it can be expressed as 2^k where k >= 1.
    """
    # Using bitwise operator to check if number is power of 2
    if (num & (num-1))==0:
        return "Yes, number can be expressed as 2^k"
    else:
        return "No, number cannot be expressed as 2^k"

 


# test case
print(power_of_two_sol_one(32))
print(power_of_two_sol_two(32))