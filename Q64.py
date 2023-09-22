# 64. Write a Python program to calculate the surface volume and area of a cylinder.

import math

def calculate_cylinder_surface_area(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    
    total_surface_area = (2 * math.pi * radius**2) + lateral_surface_area
    
    return lateral_surface_area, total_surface_area

def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

lateral_surface_area, total_surface_area = calculate_cylinder_surface_area(radius, height)
volume = calculate_cylinder_volume(radius, height)

print(f"Lateral Surface Area: {lateral_surface_area:.2f}")
print(f"Total Surface Area: {total_surface_area:.2f}")
print(f"Volume: {volume:.2f}")
