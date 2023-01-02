
# program to find sum of multiple numbers with arbitrary arguments

def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    return  result



result = find_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Sum is : ", result)


result = find_sum(123, 456)
print("Sum is : ", result)