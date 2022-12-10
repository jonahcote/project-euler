# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Strategy:
# Build a list of all prime numbers below half of n
#   - Sieve of Eratosthenes - eliminate multiples of 2, 3, 4...
#   - start out with array of 1s of size n/2
#   - for each index that's a multiple of m, change the value to 0
#   - repeat, increasing index by 1 up to n/2
#   - at the end, all remaining 1 values are prime
# Build a list of all factors of n
#   - start out with array of 0s of size n/2
#   - for each factor f, if f % n == 0, set value to a 1
# Find matches of the prime number array and factor array
#   - for each item equal to 1 in array primes, check corresponding index in array factors
#   - if match, add to array matches
# Take the last value of that arrray and return it

# imports
import numpy as np

# define main
def main():
    n = 13195
    primes = np.array(generatePrimes(n), dtype=np.int64)
    factors = np.array(generateFactors(n), dtype=np.int64)
    overlap = np.array([], dtype=np.int64)
    overlap = np.intersect1d(primes, factors)
    print("Overlap:\n",overlap)
    final = overlap[-1]
    print(final)



# Build a list of all prime numbers below half of n
def generatePrimes(n):
    # Sieve of Eratosthenes - eliminate multiples of 2, 3, 4...
    # start out with array of 1s of size n/2
    a = np.ones((n//2), dtype=np.int16)
    # for each index that's a multiple of m, change the value to 0
    m = 2
    while (m < n//2):
        i = 2
        while (i*m < n//2):
            a[i*m] = 0
            i += 1
        m += 1
    
    # return array of 1 value indexes (array of just primes)
    for i in range(len(a)):
        if a[i] == 1:
            a[i] = i
    a = a[a != 0]
    return(a)

def generateFactors(n):
    # create an array of zeros
    a = np.array([], dtype=np.int16)
    # we have 500 zeros
    # we need to find numbers that are factors of n
    # for every number 2-n//2, run n % that number == 0
    i = 2
    while(i <= n//2):
        
        if(n % i == 0):
            a = np.append(a, i)
        i += 1
    return a

# call main
main()