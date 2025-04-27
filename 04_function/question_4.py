# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math


def circle_info(radius):
    # Calculate area
    area = math.pi * radius ** 2
    # Calculate circumference
    circumference = 2 * math.pi * radius
    return area, circumference


# Example usage
radius = 5
area, circumference = circle_info(radius)
print(f"Area: {area}, Circumference: {circumference}")
