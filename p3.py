# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# imports
import numpy as np
import math

# define main
def main():

    n = 600851475143
    gpf = 1

    # check every i between 2 and sqrt(n)
    i = 2
    ceiling1 = math.sqrt(n)
    print("n\t",n,"\ngpf\t",gpf,"\ni\t",i,"\nc1\t",ceiling1,"\n")
    while(i <= ceiling1):
        # check if i is a factor of n
        if(n % i == 0):
            print("Factor found:",i)
            # if so, check if i has any factors between 2 and sqrt(i)
            j = 2
            ceiling2 = math.sqrt(i)
            while(j <= ceiling2):
                if(i % j == 0):
                    # if so, it's not prime
                    break
                j += 1
            # if not at the end, replace gpf with i
            else:
                print("\t\t\t",i,"is prime.")
                gpf = i
        i += 1

    print("\n=======\nFINAL:",gpf,"\n")

# call main
main()