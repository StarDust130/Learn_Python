# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Age: "))
day = input("Enter Day: ").strip().lower()

# Base price based on age
price = 12 if age >= 18 else 8

# Apply $2 discount if it's Wednesday
if day in ["wednesday", "wed"]:
    price -= 2

print(f"Your Ticket Price is ${price}")
