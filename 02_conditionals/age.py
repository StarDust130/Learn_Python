# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter your age: "))

if(age < 13):
    age_group = "Child"
elif(age < 20):
    age_group = "Teenager"
elif(age < 60):
    age_group = "Adult"
else:   
    age_group = "Senior"


print(f"You are classified as: {age_group}")

