# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Age: "))
day = str(input("Enter Day: ").strip().lower())

if age >= 10:
    price = 12
else:
    price = 8

if day == "wednesday" or day == "wed":
    price -= 2


print(f"Your Ticket Price is {price}")


