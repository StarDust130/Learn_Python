# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


color = input("Enter Banana Color: ").strip().lower()

banana_quality = {
    "green": "Unripe",
    "yellow": "Ripe",
    "brown": "Overripe"
}

quality = banana_quality.get(color, "Unknown")

print(f"Banana Quality is: {quality}")
