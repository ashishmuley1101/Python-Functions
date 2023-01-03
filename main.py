
# Returning even numbers using lambda and filter() function

numbers = [11, 222, 123, 445, 550, 612, 776, 888, 960, 101]

# filter() returning the numbers object we have to convert filter() into list()
even_number = list(filter(lambda n : n%2 == 0, numbers))

print("Even numbers are : ", even_number)