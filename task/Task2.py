# Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area = π×r ^ 2
# ``` (Take pie as 3.14)

Radius_of_circle = float(input("enter the value"))
pi = float(input("pi value"))
area = pi * Radius_of_circle ** 2
print(f"area of radius{Radius_of_circle} is {area}")