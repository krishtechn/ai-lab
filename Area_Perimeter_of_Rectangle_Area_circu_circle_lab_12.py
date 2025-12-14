# Program to calculate area & perimeter of rectangle
# and area & circumference of circle

import math

# Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

rect_area = length * breadth
rect_perimeter = 2 * (length + breadth)

print("\nRectangle Results:")
print("Area:", rect_area)
print("Perimeter:", rect_perimeter)

# Circle
radius = float(input("\nEnter radius of circle: "))

circle_area = math.pi * radius * radius
circle_circumference = 2 * math.pi * radius

print("\nCircle Results:")
print("Area:", circle_area)
print("Circumference:", circle_circumference)
