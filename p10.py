# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

# define main
def main():

    running_sum = 0

    max_value = 2000000

    # iterate through all numbers 2-n
    for candidate in range(2,max_value):
        # counter to check progress
        if(candidate % 100000 == 0):
            print("Checking",candidate,"\tRunning Sum:",running_sum)

        # reset is_prime
        is_prime = True

        # print(candidate,math.sqrt(candidate),int(math.sqrt(candidate)))

        # check if the candidate is prime
        for j in range(2,int(math.sqrt(candidate))+1):
            # print("Checking",candidate,"%",j,":",candidate % j == 0)
            if(candidate % j == 0):
                is_prime = False

        if(is_prime == True):
            # print("Adding",candidate)
            running_sum += candidate

    print("Sum:",running_sum)
    
    return True

# call main
main()