
# Square for the given numbers using lambda function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = []

square = lambda n : n ** 2

for n in numbers:
    square_numbers.append(square(n))

print("Square of numbers : ", square_numbers)