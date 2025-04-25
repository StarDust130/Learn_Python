# Problem: Given a list of numbers, count how many are positive.


numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10, 5]

count = 0

for i in numbers:
    if i >= 0:
        count += 1

print(f"Postive Number in List is {count}")


