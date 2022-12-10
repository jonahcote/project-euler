# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

startingFactors = [3, 5]

limit = 1000

def main():
    print(sumMultiples(startingFactors, limit))

def sumMultiples(sf, l):
    # start sum at zero
    sum = 0

    # check every sum up to limit (l) if it is a multiple of the starting factors (sf)
    for i in range(1, l):
        for f in sf:
            if i % f == 0:
                sum += i
                break

    return sum

main()