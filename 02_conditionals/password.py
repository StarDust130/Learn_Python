# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter Password: ").strip()
length = len(password)

if length < 6:
    strength = "Weak"
elif length >= 6 and length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Your Password is {strength}")
