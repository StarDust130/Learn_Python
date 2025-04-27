#  Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2 ,3 , 4 ,5))