# Compute the factorial of a number using a while loop.

num = int(input("Enter a number: "))

factorial = 1
while num > 0:
    factorial = factorial * num
    num = num - 1

print("Factorial is:", factorial)
