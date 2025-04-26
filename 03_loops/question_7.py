# Keep asking the user for input until they enter a number between 1 and 10.


while True:
    num = int(input("Enter a number: "))
    if num > 0 and num <= 10:
        break
