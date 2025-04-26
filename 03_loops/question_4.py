# Problem: Reverse a string using a loop.

str = str(input("Enter your dost ka Naam: "))

rev_str = ""

for char in str:
    rev_str = char + rev_str

print(rev_str)    