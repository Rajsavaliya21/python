# 63. Write a Python program to calculate the area of a parallelogram.

def parallelogram_area(base, height):
    area = base * height
    return area

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = parallelogram_area(base, height)

print(f"The area of the parallelogram is: {area:.2f}")
