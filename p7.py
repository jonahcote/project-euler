# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import numpy as np

# Define main
def main():
    generatePrimeCountOf(10001)
    return True

# Build a list of all prime numbers below half of n
def generatePrimeCountOf(primeCount):

    count = 0
    potentialPrime = 1
    isPrime = True

    while (count <= primeCount):
        # add 1 to potential prime
        potentialPrime += 1

        # reset i and isPrime
        isPrime = True
        
        # check if the potential prime has any factors besides itself and 1
        for i in range(2,potentialPrime):
            if (potentialPrime % i == 0):
                #print(potentialPrime,"is NOT prime")
                isPrime = False
                break
            i += 1
        
        # increase the count for valid primes
        if (isPrime):
            count += 1

        # print out every 1000 primes found to keep tabs on program progress
        if (isPrime and count % 1000 == True):
            print (">>>",potentialPrime, "is prime number",count)

        if (isPrime and count == primeCount):
            print("Prime number",count,"is",potentialPrime)

    return True

# Call main
main()