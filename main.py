
# program to find sum of multiple numbers with arbitrary arguments

def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    return  result


# function call with 3 arguments
result = find_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Sum is : ", result)

# function call with 2 arguments
result = find_sum(123, 456)
print("Sum is : ", result)