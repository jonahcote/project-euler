# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0

for i in range(1,100):
    print("Adding",i**2)
    sum_of_squares += i ** 2
print("Sum of squares:",sum_of_squares)

sum_of_natural_numbers = 0

for i in range(1,100):
    print("Adding",i**2)
    sum_of_natural_numbers += i
print("Sum of natural numbers:",sum_of_natural_numbers)

square_of_sum = sum_of_natural_numbers ** 2
print("Square of sum:",square_of_sum)

print(abs(square_of_sum-sum_of_squares))