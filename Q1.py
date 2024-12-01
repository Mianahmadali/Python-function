#Write a Function To calculate the area of a circle given its radius.
import math

def calculate_area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    area = math.pi * (radius ** 2)
    return area

# Example usage:
radius = 10
area = calculate_area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")