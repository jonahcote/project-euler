# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# How many checks can we save?
    # If 20, then 1, 2, 4, 5, 10, 20
    # If 18, then 9, 18
    # If 16, then 8, 16
    # If 14, then 7, 14
    # If 12, then 3, 6, 12
    # Remainder: 11 13 15 17 19
# These are just every number 11-20
# 11, 13, 17, and 19 are prime, so the combined number must be a multiple of the product of those primes (46189)

# def main
def main():
    # start at 19
    n = 11

    # initialize booleans
    found = False
    accepted = True

    # loop through all numbers until successful
    while(found == False):
        # reset accepted
        accepted = True
        # check factors 12-20 (all numbers below 11 are also factors of numbers 11-20 and don't have to be counted, and we only operate on multiples of 11)
        for i in range(2, 10):
            # are any factors missing?
            if(not(n % (10+i) == 0)):
                # if so, do not accept number
                accepted = False
                # break to save time on useless checks
                break
        # if all factors have been checked and number still passes, print the number and stop the loop
        if (accepted):
            print(n)
            found = True
        # print out every 11 million to check program progress
        if(n % 1000000 == 0):
            print(n)
        # increase the count by 19
        # (19 is chosen as it's a rare combination with other factors and allows us to check 12-10 instead of 11-20, saving time)
        n += 11

# call main
main()