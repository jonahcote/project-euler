# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# functions
def main():

    baseNums = 3
    
    startF1 = int("9"*baseNums)
    startF2 = int("9"*baseNums)

    f1 = startF1
    f2 = startF2
    max = 0

    # starting at top, move down
    while (f1 > 800):
        f2 = startF2
        while (f2 > 800):
            # print(f1, f2)
            # create product
            p = f1 * f2
            # check if palindrome
            if(str(p) == str(p)[::-1]):
                if(p > max):
                    max = p
                    print("New max:",max)
            f2 -= 1
        f1 -= 1

    return True

# call main
main()