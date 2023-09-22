# Write a Python program to find the second smallest number in a list.

l=[1,8,3,4,5,3,3,2,2,1]
first_min=min(l)
print(first_min)
second_min=l[0]
for i in l :
    if second_min==first_min:
        second_min=i
for i in l :
    if second_min>i and i!=first_min:
        second_min=i
print(second_min)

