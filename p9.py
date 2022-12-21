# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def main():

    # Find all a < b < c while a+b+c=1000

    a = 0
    b = 1
    c = 999

    for i in range(665):
        print ("Sum",a+b+c,"\tChecking",a,b,c)
        if (i%2==0):
            b += 1
        else:
            a += 1
        c -= 1

        if (a**2 + b**2 == c**2):
            print("\tFOUND:",a, b, c)
            break

    # Check if a^2 + b^2 = c^2
    return True



main()