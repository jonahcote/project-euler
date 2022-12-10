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

# define main
def main():
    generatePrimes(1000)

# Build a list of all prime numbers below half of n
def generatePrimes(n):
    # Sieve of Eratosthenes - eliminate multiples of 2, 3, 4...
    # start out with array of 1s of size n/2
    startArray = []
    for i in range(n//2):
        startArray.append(1)
    # for each index that's a multiple of m, change the value to 0
    m = 2
    while (m < n//2):
        i = 2
        while (i*m < n//2):
            startArray[i*m] = 0
            # print("Removed value at:",i*m)
            i += 1
        m += 1
    print(startArray)
    
    # return array of 1 value indexes (array of just primes)
    for i in range(len(startArray)):
        if startArray[i] == 1:
            startArray[i] = i
            
    print(startArray)

# call main
main()