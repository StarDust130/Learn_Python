#  Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet(name="Lalulal", Lage=25, city="New Delhi")
