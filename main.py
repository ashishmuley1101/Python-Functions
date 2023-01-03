
# Square for the given numbers using lambda and map() function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() returning the numbers object we have to convert map() into list()
square = list(map(lambda n : n ** 2, numbers))

print("Square of numbers : ", square)