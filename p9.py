# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def main():

    # Find all a < b < c while a+b+c=1000

    a = 0
    b = 0
    c = 1000

    found = False

    # Decrease c
    while (c>0 and not found):
        c = c - 1
        b = 1000 - c
        a = 0
        while (c>333 and b>a):
            #print("Testing",a,b,c)
            if(c>b>a and b != 500 and isPythagoreanTriple(a,b,c)):
                print("Found!",a,b,c)
                found = True
                break
            b = b - 1
            a = a + 1


def isPythagoreanTriple(a, b, c):
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False

main()