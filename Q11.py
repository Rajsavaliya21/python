# Write a Python program to generate and print a list of the first and last 5 elements, where the values are the squares of numbers between 1 and 30.

list_sq=[]
for i in range(1,31):
    list_sq.append(i*i)
print(list_sq[0:6],"  " , list_sq[-5:])
print(list_sq)
