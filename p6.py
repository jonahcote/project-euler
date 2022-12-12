# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

start_value = 1
end_value = 100

sum_of_squares = 0
sum_of_natural_numbers = 0
square_of_sum = 0

# Find the sum of the squares
# Iterate through each natural number, square it, and add it to sum_of_squares 
for i in range(start_value, end_value+1):
    #print("Adding",i**2)
    sum_of_squares += i ** 2
#print("Sum of squares:",sum_of_squares)


# Find the square of the sum
# Itereate through each natural number, and add it to sum_of_natural_numbers
for i in range(start_value, end_value+1):
    #print("Adding",i)
    sum_of_natural_numbers += i
#print("Sum of natural numbers:",sum_of_natural_numbers)

square_of_sum = sum_of_natural_numbers ** 2
#print("Square of sum:",square_of_sum)

print("Difference:",abs(square_of_sum-sum_of_squares))