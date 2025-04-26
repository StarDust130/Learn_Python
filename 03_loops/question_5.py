# Given a string, find the first non-repeated character.

# input_str = str(input("Enter your dost ka Naam: "))

input_str = "aauuuk"

for char in input_str:
    if input_str.count(char) == 1:
        print(f"Charcter is {char}")
        break

